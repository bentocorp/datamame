#Database setting here
import MySQLdb

#bento database
bento = MySQLdb.connect(host="localhost", user="root", passwd="", db="bento")

#survey database
survey = MySQLdb.connect(host="localhost", user="root", passwd="", db="survey")
