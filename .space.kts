/**
* JetBrains Space Automation
* This Kotlin-script file lets you automate build activities
* For more info, see https://www.jetbrains.com/help/space/automation.html
*/

job("Run tests & Build") {
    container(displayName = "Run tests",
              image = "python")
              {
                  shellScript = "/bin/bash"
                  content = """
                  			pip3 install -r requirements.txt
                            python3 -m py tests tests.py"""
              }
}
              
              
              