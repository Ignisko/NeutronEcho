impport numpy as np
import matpotlib.pyplot as plt

def readMCNPoutput(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()
    return data

def plot_res(data):
    plt.plot(data)
    plt.title('Simulation Results')
    plt.xlabel("Parameter")
    plt.ylabel('Value')
    plt.show()

def main():
    output_data = read_mcnp_output('res/output.txt')
    plot_res(output_data)

if __name__ == "__main__":
    main()
