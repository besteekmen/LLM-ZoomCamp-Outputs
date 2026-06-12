# **Overall Setup Plan**
These are the setup steps for a Windows 11 Pro laptop with Visual Studio Code, Python 3.13 and Git preinstalled.
## 1. Verify Python version
Open PowerShell (not Command Prompt) and run:
```python
python --version
```
or if that fails 
```python
py --version
```

If the version is 3.10+, it already satisfies the Zoomcamp requirement.

## 2. Install uv
```uv``` is used for Python dependency management in Zoomcamp projects and it won't interfere with existing PyCharm/VS Code projects using ```pip``` or ```conda```. It is faster and handles virtual environments cleanly. See the [uv documentation](https://docs.astral.sh/uv/) for details.

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

The course explicitly recommends this for Windows since Docker works much more smoothly through WSL2. Before installation, check whether WSL is already installed:

```python
wsl --status
```

If it is not installed, open PowerShell as administrator and run:

```python
wsl --install
```

This installation will enable WSL (Windows Subsystem for Linux), enable Virtual Machine Platform, install WSL2 and usually install Ubuntu (usually the latest LTS release). Later, reboot Windows if requested and check what is installed:
```python
wsl --list --online
```

If no Linux distribution is loaded, install one with long-term support. Here, Ubuntu 24.04 LTS is preferred.
```python
wsl --install -d Ubuntu-24.04
```
After the installation, Ubuntu will start automatically. If not, launch Ubuntu from the Start Menu and when asked, create a username and password. At the Linux prompt, run:

```python
uname -a
```
to print all available system information in a single line and 
```python
pwd
```
to print the working directory.

## 4. Install Docker Desktop

Download the Windows installer from [Docker website](https://www.docker.com/products/docker-desktop/?utm_source=chatgpt.com). While running the installer, make sure "Use WSL 2 instead of Hyper-V" is checked. Reboot if requested. After signing in, verify that Docker and WSL are connected correctly. In Docker Desktop, go to Settings -> Resources -> WSL Integration and enable the downloaded Ubuntu version. 

![Docker WSL integration](images/docker_wsl.png)

To test Docker in Ubuntu, launch Ubuntu and run:
```python
docker --version
```
```python
docker run hello-world
```
which will print a Docker version, download a small image, run a container and print a "Hello from Docker!" message.

## 5. Verify Git

Check whether git is already installed in Ubuntu with:
```python
git --version
```

## 6. Create a dedicated Zoomcamp workspace

In Ubuntu, create a separate folder from your existing projects dedicated to zoomcamp:

```python
mkdir -p ~/zoomcamp
cd ~/zoomcamp
pwd
```

## 7. Configure VS Code for WSL
To check and install VS Code Server for Linux, in Ubuntu, run:

```python
code .
```
This will allow editing Linux files from Windows.

## 8. Install Jupyter support

Needed for notebooks. Avoid installing Jupyter globally to prevent a mess of kernels and environments. It's better to install Jupyter inside the Zoomcamp project environment when the course actually needs it.

## 9. Choose and configure an LLM provider

Pick OpenAI to experience with the industry-standard API. Go to [OpenAI Platform](https://platform.openai.com/?utm_source=chatgpt.com):
- Sign in (or create an account).
- Go to the desired project.
- Add a small amount of credit (e.g. $5–10).
- Create an API key.
- Save the API key somewhere safe when it is shown. **OpenAI only shows the full key once.**

## 10. Clone the Zoomcamp repository

## Notes:
Deferred until needed
⏳ OpenAI API key
⏳ Jupyter
⏳ Module-specific dependencies
