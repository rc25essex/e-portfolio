package com.threadsafe;

import org.junit.jupiter.api.Test;

import java.math.BigDecimal;

import static org.junit.jupiter.api.Assertions.*;

/**
 * Unit tests for the BankAccount class.
 */
class BankAccountTest {

    @Test
    void shouldDepositMoney() {
        BankAccount account = new BankAccount("ACC001", new BigDecimal("1000.00"));

        account.deposit(new BigDecimal("200.00"));

        assertEquals(new BigDecimal("1200.00"), account.getBalance());
    }

    @Test
    void shouldWithdrawMoney() {
        BankAccount account = new BankAccount("ACC001", new BigDecimal("1000.00"));

        boolean result = account.withdraw(new BigDecimal("300.00"));

        assertTrue(result);
        assertEquals(new BigDecimal("700.00"), account.getBalance());
    }

    @Test
    void shouldRejectWithdrawalWhenInsufficientFunds() {
        BankAccount account = new BankAccount("ACC001", new BigDecimal("100.00"));

        boolean result = account.withdraw(new BigDecimal("200.00"));

        assertFalse(result);
        assertEquals(new BigDecimal("100.00"), account.getBalance());
    }

    @Test
    void shouldTransferMoneyBetweenAccounts() {
        BankAccount john = new BankAccount("ACC001", new BigDecimal("1000.00"));
        BankAccount friend = new BankAccount("ACC002", new BigDecimal("500.00"));

        boolean result = john.transferTo(friend, new BigDecimal("100.00"));

        assertTrue(result);
        assertEquals(new BigDecimal("900.00"), john.getBalance());
        assertEquals(new BigDecimal("600.00"), friend.getBalance());
    }

    @Test
    void shouldRejectTransferWhenInsufficientFunds() {
        BankAccount john = new BankAccount("ACC001", new BigDecimal("50.00"));
        BankAccount friend = new BankAccount("ACC002", new BigDecimal("500.00"));

        boolean result = john.transferTo(friend, new BigDecimal("100.00"));

        assertFalse(result);
        assertEquals(new BigDecimal("50.00"), john.getBalance());
        assertEquals(new BigDecimal("500.00"), friend.getBalance());
    }

    @Test
    void shouldRejectNegativeInitialBalance() {
        IllegalArgumentException exception = assertThrows(
                IllegalArgumentException.class,
                () -> new BankAccount("ACC001", new BigDecimal("-100.00"))
        );

        assertEquals("Initial Balance cannot be negative.", exception.getMessage());
    }

    @Test
    void shouldRejectBlankAccountNumber() {
        IllegalArgumentException exception = assertThrows(
                IllegalArgumentException.class,
                () -> new BankAccount("", new BigDecimal("100.00"))
        );

        assertEquals("Account number cannot be empty.", exception.getMessage());
    }

    @Test
    void shouldHandleConcurrentDeposits() throws InterruptedException {
        BankAccount account = new BankAccount("ACC001", BigDecimal.ZERO);

        Thread t1 = new Thread(() -> account.deposit(new BigDecimal("100.00")));
        Thread t2 = new Thread(() -> account.deposit(new BigDecimal("100.00")));
        Thread t3 = new Thread(() -> account.deposit(new BigDecimal("100.00")));

        t1.start();
        t2.start();
        t3.start();

        t1.join();
        t2.join();
        t3.join();

        assertEquals(new BigDecimal("300.00"), account.getBalance());
    }

    @Test
    void shouldAvoidDeadlockDuringMutualTransfers() throws InterruptedException {
        BankAccount john = new BankAccount("ACC001", new BigDecimal("1000.00"));
        BankAccount friend = new BankAccount("ACC002", new BigDecimal("500.00"));

        Thread t1 = new Thread(() -> john.transferTo(friend, new BigDecimal("100.00")));
        Thread t2 = new Thread(() -> friend.transferTo(john, new BigDecimal("50.00")));

        t1.start();
        t2.start();

        t1.join(1000);
        t2.join(1000);

        assertFalse(t1.isAlive());
        assertFalse(t2.isAlive());

        assertEquals(new BigDecimal("950.00"), john.getBalance());
        assertEquals(new BigDecimal("550.00"), friend.getBalance());
    }
}