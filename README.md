# Rigorous Two Phase Locking Protocol

This Python program implements the Rigorous Two Phase Locking (2PL) Protocol. The 2PL protocol is a concurrency control mechanism used in database systems to ensure serializability and avoid conflicts between transactions.

## Features

- **Read and Write Operations**: Transactions can perform read and write operations on variables.
- **Commit and Abort**: Transactions can commit or abort, indicating the completion or termination of the transaction.
- **Resource Table**: Provides information about the status of resources (variables) and their corresponding transactions.
- **Log Table**: Displays the log of operations performed and their corresponding transactions.

## Usage

1. Run the program: `python main.py`
2. Enter the operations in the specified format. Use the following guidelines:
   - Read Operation: `r<transaction_id><variable>`
   - Write Operation: `w<transaction_id><variable>`
   - Commit: `C<transaction_id>C`
   - Abort: `A<transaction_id>A`

Example: `r1a, w2a, C1C, r2b, w3a, r2a, w3b, r3c, C3C, C2C`

3. View the output, which includes the raw log, resource table, and log table.

## Output

### Raw Log

Displays the sequence of operations performed by transactions.

### Resource Table

Provides information about the status of resources (variables) and their corresponding transactions. The table includes the resource name, status (Shared/Exclusive/Free), and the transaction holding the lock.

### Log Table

Displays a log of the operations performed, including the type of operation (Shared Lock, Exclusive Lock, WAIT, RESCHEDULED, COMMIT, or ABORT), the resource name, and the corresponding transaction.

