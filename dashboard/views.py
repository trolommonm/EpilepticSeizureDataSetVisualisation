from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from dashboard.Data import getSeizureData, getNonSeizureData, getColumns, getSeizureHtml, getNonSeizureHtml
from dashboard.Data import getFTColumns, getSeizureFTData, getNonSeizureFtData, getSeizureFtHtml, getNonSeizureFtHtml
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

columns = getColumns()
seizureData = getSeizureData()
nonSeizureData = getNonSeizureData()
htmlSeizure = getSeizureHtml(columns, seizureData[0])
htmlNonSeizure = getNonSeizureHtml(columns, nonSeizureData[0])

columnsFt = getFTColumns()
seizureFtData = getSeizureFTData()
nonSeizureFtData = getNonSeizureFtData()
htmlSeizureFt = getSeizureFtHtml(seizureFtData[0])
htmlNonSeizureFt = getNonSeizureFtHtml(nonSeizureFtData[0])

def beforeFT(request):
	context = {
		'columns': columns,
		'seizure': seizureData,
		'nonSeizure': nonSeizureData,
		'plotHtmlSeizure': htmlSeizure,
		'plotHtmlNonSeizure': htmlNonSeizure 
	}

	return render(request, 'dashboard/beforeft.html', context)

def afterFT(request):
	context = {
		'columns': columnsFt,
		'seizureFt': seizureFtData,
		'nonSeizureFt': nonSeizureFtData,
		'plotHtmlSeizureFt': htmlSeizureFt,
		'plotHtmlNonSeizureFt': htmlNonSeizureFt
	}

	return render(request, 'dashboard/afterft.html', context)

@csrf_exempt 
def requestHtmlSeizure(request):
	if request.method == 'POST':
		jsonStr = request.body.decode("utf-8")
		data = json.loads(jsonStr)
		x = getSeizureHtml(columns, seizureData[int(data['id'])])
		return JsonResponse({'html': x}, status=200)

@csrf_exempt 
def requestHtmlNonSeizure(request):
	if request.method == 'POST':
		jsonStr = request.body.decode("utf-8")
		data = json.loads(jsonStr)
		x = getNonSeizureHtml(columns, nonSeizureData[int(data['id'])])
		return JsonResponse({'html': x}, status=200)

@csrf_exempt 
def requestHtmlSeizureFt(request):
	if request.method == 'POST':
		jsonStr = request.body.decode("utf-8")
		data = json.loads(jsonStr)
		x = getSeizureFtHtml(seizureFtData[int(data['id'])])
		return JsonResponse({'html': x}, status=200)

@csrf_exempt 
def requestHtmlNonSeizureFt(request):
	if request.method == 'POST':
		jsonStr = request.body.decode("utf-8")
		data = json.loads(jsonStr)
		x = getNonSeizureFtHtml(nonSeizureFtData[int(data['id'])])
		return JsonResponse({'html': x}, status=200)