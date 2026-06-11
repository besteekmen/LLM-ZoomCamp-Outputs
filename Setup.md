# **Overall Setup Plan**
This is the setup steps for a Windows 11 Pro laptop with Visual Studio Code, Python 3.13 and Git preinstalled.
## 1. Verify Python version
Open PowerShell (not Command Prompt) and run:
```python
python --version
```
or if that fails 
```python
py --version
```

If version is 3.10+, it already satisfies the Zoomcamp requirement.

## 2. Install uv
```uv``` is used for Python dependency management in Zoomcamp projects and it won't interfere with existing PyCharm/VS Code projects using ```pip``` or ```conda```. It is faster and handles virtual environments cleanly. See the [uv documentation]([https://docs.github.com](https://docs.astral.sh/uv/)) for details.

Open PowerShell and run: 

```python
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
After it finishes, close PowerShell completely and open a new PowerShell window to verify:

```python
uv --version
```
If the version appears, the requirement is satisfied.

## 3. Install WSL2 + Ubuntu

The course explicitly recommends this for Windows. Docker works much more smoothly through WSL2.

## 4. Install Docker Desktop

Configure it to use WSL2.

## 5. Verify Docker works inside Ubuntu

Run a test container.

## 6. Install Git (if not already installed)
## 7. Create a dedicated Zoomcamp workspace

Separate folder from your existing projects.

## 8. Configure VS Code for WSL

Allows editing Linux files from Windows.

## 9. Install Jupyter support

Needed for notebooks.

## 10. Choose and configure an LLM provider

OpenAI if you want experience with the industry-standard API.
## 11. Clone the Zoomcamp repository
