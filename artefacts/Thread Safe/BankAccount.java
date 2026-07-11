package com.threadsafe;

import java.math.BigDecimal;

/**
 * Thread-safe bank account implementation supporting
 * deposits, withdrawals and transfers between accounts.
 */
public class BankAccount {

    private final String accountNumber;
    private BigDecimal balance;

    /**
     * Creates a new bank account with the specified account number
     * and opening balance.
     *
     * @param accountNumber  unique identifier for the account
     * @param initialBalance starting account balance
     * @throws IllegalArgumentException if the account number is blank
     *                                  or the initial balance is negative
     */
    public BankAccount(String accountNumber, BigDecimal initialBalance) {
        if (accountNumber == null || accountNumber.isBlank()) {
            throw new IllegalArgumentException("Account number cannot be empty.");
        }

        if (initialBalance == null || initialBalance.compareTo(BigDecimal.ZERO) < 0) {
            throw new IllegalArgumentException("Initial Balance cannot be negative.");
        }

        this.accountNumber = accountNumber;
        this.balance = initialBalance;
    }

    /**
     * Synchronized to prevent race conditions when updating balance.
     */
    public synchronized boolean deposit(BigDecimal amount) {
        if (amount == null || amount.compareTo(BigDecimal.ZERO) <= 0) {
            throw new IllegalArgumentException("Deposit Amount must be greater than zero");
        }

        balance = balance.add(amount);
        return true;
    }

    /**
     * Synchronized to ensure only one thread can withdraw at a time.
     */
    public synchronized boolean withdraw(BigDecimal amount) {
        if (amount == null || amount.compareTo(BigDecimal.ZERO) <= 0) {
            throw new IllegalArgumentException("Withdraw amount must be greater than zero.");
        }

        if (balance.compareTo(amount) < 0) {
            return false;
        }

        balance = balance.subtract(amount);
        return true;
    }

    /**
     * Prevents deadlock by acquiring locks in a consistent
     * account-number order.
     */
    public boolean transferTo(BankAccount targetAccount, BigDecimal amount) {
        if (targetAccount == null) {
            throw new IllegalArgumentException("Target account number can not be empty.");
        }

        if (amount == null || amount.compareTo(BigDecimal.ZERO) <= 0) {
            throw new IllegalArgumentException("Transfer amount must be greater than zero.");
        }

        if (this == targetAccount) {
            throw new IllegalArgumentException("Cannot transfer to the same account.");
        }

        BankAccount firstLock;
        BankAccount secondLock;

        if (this.accountNumber.compareTo(targetAccount.accountNumber) < 0) {
            firstLock = this;
            secondLock = targetAccount;
        } else {
            firstLock = targetAccount;
            secondLock = this;
        }

        synchronized (firstLock) {
            synchronized (secondLock) {
                if (this.balance.compareTo(amount) < 0) {
                    return false;
                }

                this.balance = this.balance.subtract(amount);
                targetAccount.balance = targetAccount.balance.add(amount);
                return true;
            }
        }
    }

    /**
     * Synchronized to ensure a consistent balance is returned
     * when accessed by multiple threads.
     */
    public synchronized BigDecimal getBalance() {
        return balance;
    }

    public String getAccountNumber() {
        return accountNumber;
    }
}