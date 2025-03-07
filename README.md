PRESSURE PROJECT

This is a project that collects pressure and pulse for user
ENVIRONMENT VERIABLES:

IF
DEBUG=0 USES PRODUCT DATABASE - POSTGRESQL DATABASE
ELIF
DEBUG=1 USES DEVELOP DATABASE - SQLITE3 DATABASE

DATABASE_URL - if we use product mode in this case package dj_database_url use DATABASE_URL to connect to database
DATABASE_URL=postgresql://postgres:kCLwojVzmaItVMmtUziDPAyzVpCKBbGP@postgres.railway.internal:5432/railway
