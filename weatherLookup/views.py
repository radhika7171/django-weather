from django.shortcuts import render


# Create your views here.


def home(request):
    import json
    import requests

    if request.method == "POST":
        zipCode = request.POST['ZipCode']
        apiRequest = requests.get(
            "https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode="+  zipCode + "&distance=50&API_KEY=947048C9-8450-46A7-9892-0DDBAA623F2D")
        # parse api data in json form
        try:
            api = json.loads(apiRequest.content)
        except Exception as e:
            api = "Oooooops Error Comesssss......!!!"

        if api[0]['Category']['Name'] == "Good":
            categoryDescription = "0 to 50 : Air quality is satisfactory, and air pollution poses little or no risk."
            categoryColor = "good"
        elif api[0]['Category']['Name'] == "Moderate":
            categoryDescription = "51 to 100: Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution."
            categoryColor = "moderate"
        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
            categoryDescription = "101 to 150: Members of sensitive groups may experierience issue."
            categoryColor = "usg"
        elif api[0]['Category']['Name'] == "Unhealthy":
            categoryColor = "unhealthy"
            categoryDescription = "151 to 200: Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects."
        elif api[0]['Category']['Name'] == "Very Unhealthy":
            categoryDescription = "201 to 300: Health alert: The risk of health effects is increased for everyone."
            categoryColor = "veryUnhealthy"
        elif api[0]['Category']['Name'] == "Hazardous":
            categoryDescription = "301 and higher: Health warning of emergency conditions: everyone is more likely to be affected."
            categoryColor = "hazardous"

        return render(request, 'home.html',
                      {'api': api,
                       'categoryDescription': categoryDescription,
                       'categoryColor': categoryColor})

    else:
        apiRequest = requests.get(
            "https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=50&API_KEY=947048C9-8450-46A7-9892-0DDBAA623F2D")
        # parse api data in json form
        try:
            api = json.loads(apiRequest.content)
        except Exception as e:
            api = "Oooooops Error Comesssss......!!!"

        if api[0]['Category']['Name'] == "Good":
            categoryDescription = "0 to 50 : Air quality is satisfactory, and air pollution poses little or no risk."
            categoryColor = "good"
        elif api[0]['Category']['Name'] == "Moderate":
            categoryDescription = "51 to 100: Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution."
            categoryColor = "moderate"
        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
            categoryDescription = "101 to 150: Members of sensitive groups may experierience issue."
            categoryColor = "usg"
        elif api[0]['Category']['Name'] == "Unhealthy":
            categoryColor = "unhealthy"
            categoryDescription = "151 to 200: Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects."
        elif api[0]['Category']['Name'] == "Very Unhealthy":
            categoryDescription = "201 to 300: Health alert: The risk of health effects is increased for everyone."
            categoryColor = "veryUnhealthy"
        elif api[0]['Category']['Name'] == "Hazardous":
            categoryDescription = "301 and higher: Health warning of emergency conditions: everyone is more likely to be affected."
            categoryColor = "hazardous"

        return render(request, 'home.html',
                      {'api': api,
                       'categoryDescription': categoryDescription,
                       'categoryColor': categoryColor})


def aboutUs(request):
    return render(request, 'aboutUs.html', {})
