package com.threadsafe;

import java.math.BigDecimal;

/**
 * Simulates concurrent banking transactions using multiple threads.
 */
public class TransactionSimulator {
    public static void main(String[] args) throws InterruptedException {
        System.out.println();

        BankAccount johnAccount = new BankAccount("ACC001", new BigDecimal("1000.00"));
        BankAccount friendAccount = new BankAccount("ACC002", new BigDecimal("200.00"));

        Thread salaryPayment = new Thread(() -> {
            System.out.println("Salary deposited: "
                    + johnAccount.deposit(new BigDecimal("1200.00")));
            System.out.println("Account Balance after salary deposit is: £"
                    + johnAccount.getBalance());
        });

        Thread gasBill = new Thread(() -> {
            System.out.println("Gas bill paid: "
                    + johnAccount.withdraw(new BigDecimal("150.00")));
            System.out.println("Gas bill £5 discount deposited: "
                    + johnAccount.deposit(new BigDecimal("5.00")));
            System.out.println("Account Balance after gas bill paid and discount applied is: £"
                    + johnAccount.getBalance());
        });

        Thread electricityBill = new Thread(() -> {
            System.out.println("Electricity bill paid: "
                    + johnAccount.withdraw(new BigDecimal("80.00")));
            System.out.println("Electricity bill 5% discount deposited: "
                    + johnAccount.deposit(new BigDecimal("4.00")));
            System.out.println("Account Balance after electricity bill and discount applied is: £"
                    + johnAccount.getBalance());
        });

        Thread transferToFriend = new Thread(() -> {
            System.out.println("Transfer John -> Friend: "
                    + johnAccount.transferTo(friendAccount, new BigDecimal("100.00")));

            System.out.println("John Balance: £"
                    + johnAccount.getBalance() + "; Friend Balance: £"
                    + friendAccount.getBalance());

            System.out.println("Transfer Friend -> John: "
                    + friendAccount.transferTo(johnAccount, new BigDecimal("10.00")));

            System.out.println("John Balance: £"
                    + johnAccount.getBalance() + "; Friend Balance: £"
                    + friendAccount.getBalance());
        });

        Thread mortgage = new Thread(() -> {
            System.out.println("Mortgage payment: "
                    + (johnAccount.withdraw(new BigDecimal("2400.00"))
                    ? "processed."
                    : "Unable to process withdrawal. Insufficient funds."));

            System.out.println("Account Balance is: £"
                    + johnAccount.getBalance());
        });

        Thread balanceCheck = new Thread(() ->
                System.out.println("John checked balance: £"
                        + johnAccount.getBalance()));

        salaryPayment.start();
        gasBill.start();
        electricityBill.start();
        transferToFriend.start();
        balanceCheck.start();
        mortgage.start();

        salaryPayment.join();
        gasBill.join();
        electricityBill.join();
        transferToFriend.join();
        balanceCheck.join();
        mortgage.join();
    }
}