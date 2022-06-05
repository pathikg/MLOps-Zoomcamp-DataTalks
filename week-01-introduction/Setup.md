# Setting Up Environment for MLOps

## For Windows 

### Install WSL  
   **WSL** stands for **Windows Subsystem For linux** which allows windows users to use linux distributions in the windows  
   You can follow these instructions https://docs.microsoft.com/en-us/windows/wsl/install  
    OR  
    Follow this video : https://www.youtube.com/watch?v=X-DHaQLrBi8  
    (Optional : Use windows terminal)
### Upgrade WSL from version1 to version2  
   https://docs.microsoft.com/en-us/windows/wsl/install#upgrade-version-from-wsl-1-to-wsl-2  
   This is an essential step which is required later to use Docker in WSL  
   (This step takes around 30 mins so don't worry just stay patient and have your coffee)  
   
   After this you should be able to see this :  
   ![WSL V2](/week-01-introduction/WSL_V2.jpeg)  
   
### Install Conda/MiniConda as per your choice  
   For Conda (https://www.anaconda.com/products/distribution)
   ```bash
   wget https://repo.anaconda.com/archive/Anaconda3-2022.05-Linux-x86_64.sh
   bash Anaconda3-2022.05-Linux-x86_64.sh
   ```
   For MiniConda (https://docs.conda.io/en/latest/miniconda.html#linux-installers)  
   ```bash
   wget https://repo.anaconda.com/miniconda/Miniconda3-py39_4.12.0-Linux-x86_64.sh 
   bash Miniconda3-py39_4.12.0-Linux-x86_64.sh
   ```
### Install Docker
   ```bash
   sudo apt install docker.io
   ```
   Running Docker without `sudo`
   ```bash
   sudo groupadd docker
   sudo usermod -aG docker $USER
   ```
### Install Docker Compose  
   Installing in separate folder
   ```bash
   mkdir soft
   cd soft
   ```
   From https://github.com/docker/compose, get the latest release for linux and then  
   ```bash
   wget https://github.com/docker/compose/releases/download/v2.5.0/docker-compose-linux-x86_64 -O docker-compose
   ```
   Make it Executable 
   ```bash
   chmod +x docker-compose
   ```
   Add to the soft directory to PATH. Open the .bashrc file with nano:
   ```bash
   nano ~/.bashrc
   ```
   In .bashrc, add the following line:
   ```bash
   export PATH="${HOME}/soft:${PATH}"
   ```
   
   ![Soft Path](/week-01-introduction/soft_path.jpg) 
   
   Save it and run the following to make sure the changes are applied:
   ```bash
   source .bashrc
   ```
### Install Docker Desktop on windows  
   Just follow this : https://docs.docker.com/desktop/windows/wsl/  
   ;)
### Test the setup  
   ![test](/week-01-introduction/test_setup.jpg)  
   
## For Linux 
    Everything same as the Windows installation from Step 3 

And we are good to go !
