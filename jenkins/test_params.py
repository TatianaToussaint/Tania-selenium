def test_parameters(request):
    browser = request.config.getoption("--browser")
    os = request.config.getoption("--OS")

    print(f"OS on test server is {os}")
    if browser == "Chrome":
        print("Start Chrome")
    elif browser == "Firefox":
        print("Start Firefox")
    elif browser == "Edge":
        print("Start Edge")

