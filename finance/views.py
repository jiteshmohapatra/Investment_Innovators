from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import InvestmentForm

# Create your views here.
def project(request):
    return render(request,"index.html")

def project1(request):
    return render(request,"about.html")

def project2(request):
	return render(request,"team.html")

def project3(request):
	return render(request,'calculator/feature1.html')



def calculate_savings(request):
    if request.method == 'POST':
        income = float(request.POST['income'])
        expenses = float(request.POST['expenses'])
        savings = income - expenses
        return render(request, 'calculator/calculate1.html', {'savings': savings})
    return render(request, 'calculator/calculate.html')


















class Index(View):
	def get(self, request):
		form = InvestmentForm()
		return render(request, 'calculator/index2.html', {'form': form})

	def post(self, request):
		form = InvestmentForm(request.POST)

		if form.is_valid():
			total_result = form.cleaned_data['starting_amount']
			total_interest = 0
			yearly_results = {}

			for i in range(1, int(form.cleaned_data['number_of_years'] + 1)):
				yearly_results[i] = {}

				# calculate the interest
				interest = total_result * (form.cleaned_data['return_rate'] / 100)
				total_result += interest
				total_interest += interest

				# add additional contribution
				total_result += form.cleaned_data['annual_additional_contribution']

				# set yearly_results
				yearly_results[i]['interest'] = round(total_interest, 2)
				yearly_results[i]['total'] = round(total_result, 2)

				# create context
				context = {
					'total_result': round(total_result, 2),
					'yearly_results': yearly_results,
					'number_of_years': int(form.cleaned_data['number_of_years'])
				}

			# render the template
			return render(request, 'calculator/result.html', context)






