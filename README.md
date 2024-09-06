
            _____ _                     _       _ _   
            |  ___(_)_ __ ___  ___ _ __ | | ___ (_) |_ 
            | |_  | | '__/ _ \/ __| '_ \| |/ _ \| | __|
            |  _| | | | |  __/\__ \ |_) | | (_) | | |_ 
            |_|   |_|_|  \___||___/ .__/|_|\___/|_|\__|
                                    |_|                  

# FireSploit

This tool is used for education purpose don't miss use this tool!!

This tools needs configurtion setup try to insert the path of json configuration file

```javascript
{
    "apiKey": apiKey, // provided by firebase
    "projectId": projectId, // It is string if you have acces to apiKey you should no projectId
    "storageBucket": storageBucket, // usually it is "{projectId}.appspot.com"
    "authDomain": authDomain // usually it is "{projectId}.firebaseapp.com"
}
```

So to prevent an attack like this to happen an retrive all your data from datastore, add *rules*!!

> **Note:** All find data will be stored in the directory you specify even if there is interuption you progress will not be lost