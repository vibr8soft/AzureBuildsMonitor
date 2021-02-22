# AzureBuildsMonitor
This console app can monitor builds on azure. Will send you a terminal notification when your build is finish (works on Mac... still have to try on Windows).

### Configuration
Edit config.py to set your Azure personal access token. You can find how to create one on Azure [here](https://docs.microsoft.com/en-ca/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate?view=azure-devops&viewFallbackFrom=vsts&tabs=preview-page)

### Install dependencies
```Console
pip install azure-devops
pip install termcolor
```

### Launch the app
```Console
python app.py
```

#### disclaimer
This console helper is made for fun... Those are my first python lines so bear with me ;)
