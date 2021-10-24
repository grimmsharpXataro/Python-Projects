# Shodan database lookup API script 

Interactive shell using the Shodan API to search for hosts, IOT, and other things

Before using the script, you need to put your API key in the "APIKey" variable

You also need the shodan module, install it by executing :

> python -m pip install shodan 

Usage : 

    ip <host>
        Search informations for <host>
        
    search <term / exploit> <term>
        Search term / exploit results for <term>
        
    keyinfo
        Print actual key info
        
    help
        Display the help page
        
    exit
        Exip app
        
    cls
        Clear terminal
    
Examples : 
  
  > ip 193.54.67.46
  
  > search term eternalblue

