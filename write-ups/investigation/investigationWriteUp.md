
# Understanding Windows Event Logs 

## Event Viewer
- tracks everything that happens on a computer e.g hacker intruder, failed logon attempts,etc. 

**logs to look for:** 

- Application
-     log applications pertaining to applications
- Security
-      Audit failures
-     PowerShell operations
- Set-up
- System
-     the computer has stopped
-     trouble shooting something like update services

**Event ID cheatsheet:**
- https://www.ultimatewindowssecurity.com/securitylog/encyclopedia/default.aspx?i=j


  
### Enabling tracking of commands w/ info executed on PowerShell
`edit group policy > administrator template > system > audit process creation > enable include commandline process creation`
