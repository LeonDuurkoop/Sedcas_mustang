import os
from datetime import datetime
from SedCas import SedCas

def run_simulation_for_climate(model, climate_file_path, climate_file_number, start_date, end_date):
    model.climatefile = climate_file_path
    model.load_climate(start_date=start_date, end_date=end_date)
    model.load_params()
    model.run_hydro()
    model.run_sediment()
    model.save_output(climate_file_number)
    #model.plot_sedyield_monthly()

def main():
    climate_directory = r'D:\climatedata\merge\langtang'
    climate_files = [file for file in os.listdir(climate_directory) if file.startswith('climatecell.') and file.endswith('.met')]

    model = SedCas(climate_directory)
    model.paramfile = r'C:\Users\leon\Documents\sedcas\parameters.par'  # Set the parameter file path

    start_date = datetime(1951, 9, 1)  # Replace with your desired start date
    end_date = datetime(2022, 9, 30)  # Replace with your desired end date

    for climate_file_name in climate_files:
        climate_file_path = os.path.join(climate_directory, climate_file_name)
        climate_file_number = int(climate_file_name.split('.')[1])  # Extract the number from the filename

        try:
            run_simulation_for_climate(model, climate_file_path, climate_file_number, start_date, end_date)
            print(f'Simulation for climate file {climate_file_number} completed successfully.')
        except Exception as e:
            print(f'Error in simulation for climate file {climate_file_number}: {e}')

if __name__ == '__main__':
    main()
