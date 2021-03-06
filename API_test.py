import ibm_db
import ibm_db_dbi
import pandas


dsn_hostname = "" # e.g.: "dashdb-txn-sbox-yp-dal09-04.services.dal.bluemix.net"
dsn_uid = ""        # e.g. "abc12345"
dsn_pwd = ""      # e.g. "7dBZ3wWt9XN6$o0J"

dsn_driver = "{IBM DB2 ODBC DRIVER}"
dsn_database = "BLUDB"            # e.g. "BLUDB"
dsn_port = "50000"                # e.g. "50000"
dsn_protocol = "TCPIP"            # i.e. "TCPIP"

dsn = (
    "DRIVER={0};"
    "DATABASE={1};"
    "HOSTNAME={2};"
    "PORT={3};"
    "PROTOCOL={4};"
    "UID={5};"
    "PWD={6};").format(dsn_driver, dsn_database, dsn_hostname, dsn_port, dsn_protocol, dsn_uid, dsn_pwd)

# print the connection string to check correct values are specified
print(dsn)

# Create database connection

try:
    conn = ibm_db.connect(dsn, "", "")
    print("Connected to database: ", dsn_database, "as user: ", dsn_uid, "on host: ", dsn_hostname)

except:
    print("Unable to connect: ", ibm_db.conn_errormsg())

# Start

selectQuery = "select * from INSTRUCTOR"

selectStmt = ibm_db.exec_immediate(conn, selectQuery)

while ibm_db.fetch_row(selectStmt) != False:
   print(" ID:",  ibm_db.result(selectStmt, 0), " FNAME:",  ibm_db.result(selectStmt, "FIRST_NAME"))

# Using Pandas
pconn = ibm_db_dbi.Connection(conn)

pdf = pandas.read_sql(selectQuery, pconn)

print(pdf.LAST_NAME)


ibm_db.close(conn)


