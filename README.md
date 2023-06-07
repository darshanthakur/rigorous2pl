# rigorous2pl
Implementation of Rigorous Two Phase Locking Protocol in Python.

Input Format :

Enter the operations seperated by comma or spaces such that for every operation:
-First character specifies operation type (r for read or w for write)\n
-Second character specifies the Transaction ID (1-9)\n
-Third character specifies the variable on which that operation is done\n

If any transaction Commits or Aborts it can be shown as:\n
Commit: C1C \n
Abort:A1A \n

Sample Input: r1a,w2a,C1C,r2b,w3a,r2a,w3b,r3c,C3C,C2C

Output:
1. Raw Log
2. Resource Table
3. Log Table
