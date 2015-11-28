# -*- coding: utf-8 -*-
#from django.shortcuts import render
from django.shortcuts import render_to_response
from django.utils import timezone
from sample_board.models import TestBoard
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect

# Create your views here.
rowsPerPage = 5

def home(request):
	boardList = TestBoard.objects.order_by('-id')[0:10]
	currentPage = 1

	totalCount = TestBoard.objects.all().count()
	pagingHelper = PagingHelper();
	totalPageList = pagingHelper.getTotalPageList(totalCount, rowsPerPage)
	print 'totalPageList', totalPageList

	return render_to_response('page.html', {'boardList': boardList, \
			'totalCount': totalCount, 'currentPage': currentPage, \
			'totalPageList': totalPageList})

def writeForm(request):
	return render_to_response('writeForm.html')

@csrf_exempt
def registerItem(request):
	item = TestBoard(title = request.POST['title'],
				name = request.POST['name'],
				memo = request.POST['memo'],
				created_date = timezone.now(),
				hits = 0)
	item.save()

	url = '/page_work?currentPage=1'
	return HttpResponseRedirect(url)

def pageWork(request):
	currentPage = int(request.GET['currentPage'])
	totalCount = TestBoard.objects.all().count()
	print "currentPage=", currentPage

	boardList = TestBoard.objects.raw('SELECT * \
					FROM sample_board_testboard ORDER BY id DESC \
					LIMIT %s OFFSET %s',
					[rowsPerPage, (currentPage - 1) * rowsPerPage])
	print "boardList=", boardList, "count()=", totalCount

	pagingHelper = PagingHelper();
	totalPageList = pagingHelper.getTotalPageList(totalCount, rowsPerPage)

	return render_to_response('page.html', {'boardList': boardList, \
				'totalCount': totalCount, 'currentPage': int(currentPage), \
				'totalPageList': totalPageList})

class PagingHelper(object):
	def __init__(self):
		self.totalPages = 0

	def getTotalPageList(self, totalCount, rowsPerPage):
		if totalCount % rowsPerPage == 0:
			self.totalPages = totalCount / rowsPerPage
		else:
			self.totalPages = (totalCount / rowsPerPage) + 1

		self.totalPageList = []
		for i in range(self.totalPages):
			self.totalPageList.append(i + 1)

		return self.totalPageList