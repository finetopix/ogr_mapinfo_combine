import os
import subprocess


def merge_mapinfo_files(input_files, output_file):
    # Create the initial command for the first file
    print("merging mapinfo files...")
    initial_command = ['ogr2ogr', '-f', 'MapInfo File', output_file, input_files[0]]

    # Execute the initial command
    try:
        result = subprocess.run(initial_command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        #print(result.stdout.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr.decode('utf-8')}")
        return

    # Append subsequent files
    for input_file in input_files[1:]:
        command = ['ogr2ogr', '-update', '-append', output_file, input_file, '-f', '"MapInfo File"','-nln',output_file.split('.')[0]]
        #print(f"Running command: {' '.join(command)}")
        # Execute the command
        try:
            result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            #print(result.stdout.decode('utf-8'))
        except subprocess.CalledProcessError as e:
            print(f"Error: {e.stderr.decode('utf-8')}")
    for file in input_files:
        print(file,' added!')


# Example usage
if __name__ == "__main__":
    file_path = r"C:\Users\iinet\Downloads\LTE_HB_ID_52"
    os.chdir(file_path)
    input_files = ['LTE_HB_ID_53.tab', 'LTE_HB_ID_52.tab']
    output_file = 'LTE_HB_ID_AllSites.tab'
    merge_mapinfo_files(input_files, output_file)
