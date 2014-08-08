#a!/usr/bin/python
print "Content-type:text/html\n\n"

import MySQLdb
#import json
#import simplejson as json
#import collections
#import cgi
import sys

def get8601Date(d):
    if type(d) is datetime.datetime:
        s = "%04d-%02d-%02dT%02d:%02d:%02d" % (
            d.year, 
            d.month,
            d.day,
            d.hour,
            d.minute,
            d.second)
        print s
        return s
            
def print_table(results):
    print "<h1>Events</h1>"    
    print "<table border='1'>"
    print "<tr>"
    print "<td>Id</td>"
    print "<td>Name</td>"
    print "<td>Description</td>"
    print "<td>Start DateTime</td>"
    print "<td>End DateTime</td>"
    print "<td>Created DateTime</td>"
    print "<td>Created By</td>"
    print "<td>Location</td>"
    print "</tr>"
    for row in results:
        print "<tr>"
        print "<td>%s</td>" % row[0]
        print "<td>%s</td>" % row[1]
        print "<td>%s</td>" % row[2]
        print "<td>%s</td>" % row[3]
        print "<td>%s</td>" % row[4]
        print "<td>%s</td>" % row[5]
        print "<td>%s</td>" % row[6]
        print "<td>%s</td>" % row[7]
        print "</tr>"
    print "</table>"

def print_json(results, rowcount):

    try:
        
        print "<h1>json</h1>"
        ctr = 0
        js = "{"
        
        for row in results:
            ctr = ctr + 1
            js = js + '"row' + str(ctr) + '" : {'
            js = js + '"id" : "' + str(row[0]) + '", '
            js = js + '"event_name" : "' + row[1] + '", '
            js = js + '"event_description" : "' + row[2] + '", '
            js = js + '"event_start_datetime" : "' + str(row[3]) + '", '
            js = js + '"event_end_datetime" : "' + str(row[4]) + '", '
            js = js + '"event_date_created" : "' + str(row[5]) + '", '
            js = js + '"event_user_created" : "' + row[6] + '", '
            js = js + '"event_location" : "' + row[7] + '"'
            js = js + "}"
            if (ctr < rowcount):
                js = js + ","
                
        js = js + "}"
        print js
            
        #print "<h1>Results: tuple</h1>"
        #print results
        
        #print "<h1>objects_list: list of python dictionaries</h1>"
        #print objects_list
     
        #print "<h1>json</h1>"
        #print jsonstring
    
    except e:
        print "Error %d: %s" % (e.args[0], e.args[1])
        sys.exit (1)
    
try:

    print "<html>"
    print "<body>"    
    #print "<H2>Python Version: " + sys.version + "</h2>"

    # print json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
    # print "Connecting to the database"
    
    conn = MySQLdb.connect (
        host = "csrdevcocom.ipagemysql.com",
        user = "alumniassc",
        passwd = "pointbreak55",
        db = "alumni_assc_14")
        #,cursorclass = MySQLdb.cursors.SSCursor)
    
    # Open database connection
    #db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )

    # prepare a cursor object using cursor() method
    # print "Creating a cursor"
    cursor = conn.cursor()

    # execute SQL query using execute() method.
    #cursor.execute("SELECT VERSION()")
    
    # Fetch a single row using fetchone() method.
    #data = cursor.fetchone()
    #print "Database version : %s " % data
    
    #c=db.cursor()
    #max_price=5
    #c.execute("""SELECT spam, eggs, sausage FROM breakfast
    #      WHERE price < %s""", (max_price,))
    
    #cursor.execute("SELECT count(*) FROM events")
    #row = cur.fetchone()
    #print "Rowcount:" + row[0]
    #cursor.close()
    
    # print "Executing select from events"
    cursor.execute("SELECT * FROM events")
    rows_affected=cursor.rowcount
    print "<h1><font style='color:green;'>" + str(rows_affected) + "</font></h1>"
    
    # print "Fetching all data"
    results = cursor.fetchall()
    
    # print "Printing results"
    #print_table(results)
    print_json(results, rows_affected)
    
    #print type(row)
    #print results    
   
    # disconnect from server
    # print "Closing the database connection"
    cursor.close()
    conn.close()

    print "</body>"
    print "</html>"   
    
except MySQLdb.Error, e:
    print "Error %d: %s" % (e.args[0], e.args[1])
    sys.exit (1)

#print "connected to the database"

