# NeutronEcho

NeutronEcho is a cutting-edge simulation project focused on optimizing neutron shielding for microreactors. Using advanced tools like OpenMC, it analyzes and enhances shielding materials to balance safety, cost, and efficiency, ensuring robust protection against radiation in compact nuclear systems.

## Project Structure

The project is organized into the following directories:

- **`data/`**: Contains datasets, input files, and other raw data required for simulations.
- **`docs/`**: Documentation related to the project, including design documents, setup guides, and research notes.
- **`results/`**: Output files generated from simulations, such as logs, results, and analysis data.
- **`scripts/`**: Automation scripts, utility scripts, or any additional scripts that help in running simulations or processing data.
- **`src/`**: Source code for the project, including simulation setup scripts, input files for OpenMC, and any Python scripts used for pre- and post-processing.

## Getting Started

### Prerequisites

To run this project, you need the following installed on your system:

- **Windows Subsystem for Linux (WSL)**: Allows you to run a Linux environment on Windows.
- **Ubuntu**: Installed within WSL.
- **Miniconda**: A lightweight version of Anaconda that includes conda, an environment and package manager.
- **OpenMC**: An open-source Monte Carlo code for neutron transport.

### Installation

Follow these steps to set up the project on your local machine:

1. **Install WSL and Ubuntu**:
   - Follow [this guide](https://docs.microsoft.com/en-us/windows/wsl/install) to install WSL and Ubuntu.

2. **Set Up Conda Environment**:
   - Download and install Miniconda in Ubuntu:
     ```bash
     wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
     bash Miniconda3-latest-Linux-x86_64.sh
     ```
   - Follow the prompts during installation, then restart your shell:
     ```bash
     source ~/.bashrc
     ```

3. **Install OpenMC**:
   - Create a new conda environment and install OpenMC:
     ```bash
     conda config --add channels conda-forge
     conda create -n openmc-env
     conda activate openmc-env
     conda install mamba -c conda-forge
     mamba install openmc
     ```

### Running the Project

1. **Activate the Conda Environment**:
   - Before running any scripts, activate the conda environment:
     ```bash
     conda activate openmc-env
     ```

2. **Run Simulations**:
   - Navigate to the `src/` directory and run the desired simulation script using Python or directly via OpenMC.
     ```bash
     cd src/
     python simulation_setup.py
     ```
   - Alternatively, if running OpenMC directly:
     ```bash
     openmc
     ```

3. **View Results**:
   - Output results will be stored in the `results/` directory. Use analysis tools or scripts in the `scripts/` directory to process these results further.

## Contributing

If you'd like to contribute to the project, please fork the repository and use a feature branch. Pull requests are welcome.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

## Acknowledgments

- OpenMC developers for providing the Monte Carlo neutron transport code.
- The open-source community for support and contributions.

## Contact

For any questions or inquiries, please reach out to: [iggyspolski@gmail.com](mailto:iggyspolski@gmail.com)

