# AzureBuildsMonitor
This console app can monior builds on azure. Will send you a terminal notification when your build is finish.

### Configuration
Edit config.py to set your Azure personal access token. You can find how to create one on Azure [here](https://docs.microsoft.com/en-ca/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate?view=azure-devops&viewFallbackFrom=vsts&tabs=preview-page)

### Install dependancies
```Console
pip install azure-devops
pip install termcolor
```

### Launch the app
```Console
python app.py
```

#### disclaimer
This console helper is made for fun... some builds triggered by the pipeline may crash the app for the moment. some love will be added later.
