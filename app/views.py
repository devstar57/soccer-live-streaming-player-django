from django.shortcuts import render
from django.http import HttpResponse
from json import dumps
from datetime import datetime
import pymysql
import environ

env = environ.Env()
environ.Env.read_env()

conn = pymysql.connect(user=env('DATABASE_USER'), password=env('DATABASE_PASSWORD'),
                        host=env('DATABASE_HOST'), database=env('DATABASE_NAME'), cursorclass=pymysql.cursors.DictCursor)

def index(request):
    with conn.cursor() as cursor:
        sql = "SELECT * FROM stadiums WHERE id=2"
        cursor.execute(sql)
        result = cursor.fetchone()
        dataJSON = dumps(result, default=str)
        return render(request, 'index.html', {'data': dataJSON}) 

def get_player_data(request):
    strStartDateTime = request.GET["date"] + " " + request.GET["startTime"]
    strEndDateTime = request.GET["date"] + " " + request.GET["endTime"]
    startDateTime = datetime.strptime(strStartDateTime, '%Y-%m-%d %H:%M:%S')
    endDateTime = datetime.strptime(strEndDateTime, '%Y-%m-%d %H:%M:%S')
    
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM soccer WHERE time_stamp>=%s AND time_stamp<=%s", (startDateTime, endDateTime))
        result = cursor.fetchall()
        dataJSON = dumps(result, default=str)
        return HttpResponse(dataJSON)