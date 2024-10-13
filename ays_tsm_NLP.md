## Python Script Overview: AYS Model Analysis using PyViability

This document provides an extensive overview of a Python script designed to analyze the AYS model through the PyViability package, focusing on Topology of Sustainable Management (TSM) computations. It is tailored for advanced users who require detailed control over model parameters and execution settings.

### Key Components of the Script


#### 1. **Imports**
- **Standard Libraries**: `sys`, `os`, `time`, `datetime`, `argparse`, `argcomplete` for basic operations and command-line interface handling.
- **Local Modules**: `ays_general`, `ays_model` for specific functionalities and constants related to the AYS model.
- **Third-party Libraries**: `numpy`, `scipy.optimize`, `pyviability` for mathematical operations and viability analysis.

#### 2. **Global Constants and Variables**
- `MANAGEMENTS`: Defines various management strategies available for the model, indicating a modular approach to handling different management scenarios.
- `boundaries_choices`: A list that contains predefined string options representing different types of boundary conditions applicable to the model analysis. These options are crucial for ensuring the computation respects specific environmental or operational limits.
  - **Options**:
    1. `"planetary-boundary"`: Refers to boundaries set based on planetary limits, which might include factors like carbon thresholds or other ecological limits that must not be exceeded to maintain sustainability.
    2. `"social-foundation"`: Pertains to boundaries determined by social criteria, such as minimum welfare standards or other indicators that define basic quality of life or societal well-being.
    3. `"both"`: A composite option that includes both planetary and social boundaries, ensuring that the model computation considers a holistic approach to sustainability, integrating both ecological and social factors.
  

#### 3. **Command-Line Argument Parsing**
The script utilizes the Python `argparse` library to facilitate command-line argument parsing, enabling users to customize the execution of the script through various options. This feature is essential for ensuring flexibility and user control over the script's behavior during runtime. Below are the key aspects of the command-line argument parsing implemented in the script:

- **Argument Parser Initialization**: An `argparse.ArgumentParser` object is created, which serves as the foundation for building a command-line interface. The parser is described with a brief message explaining its purpose, specifically mentioning its use in analyzing the AYS model with TSM using the PyViability package.

- **Defining Arguments**:
  - **Required Arguments**:
    - `output_file`: Users must specify the path to an output file where the TSM data will be saved. This argument is crucial for determining where the computed results are stored.
  - **Optional Flags**:
    - `-b`, `--boundaries`: A mandatory choice that specifies the type of boundaries to consider during the run. It uses `choices=boundaries_choices` to restrict inputs to valid options.
    - `--no-backscaling`: A flag that, when used, instructs the script not to backscale the results after computations.
    - `-d`, `--dry-run`: Allows users to set up everything but stops short of running the TSM computation and saving the file, useful for testing.
    - `-e`, `--eddies`: Includes eddies in the computation if specified.
    - `-f`, `--force`: Forces the script to overwrite the output file if it already exists.
    - `-i`, `--integrate`: Chooses integration over linear approximation for the computation process.
    - `-n`, `--no-save`: Prevents the script from saving the results, which can be useful for testing or when output is not needed.
    - `--num`: Specifies the number of points per dimension for the grid, defaulting to a value from `ays.grid_parameters`.
    - `-p`, `--set-parameter`: Allows users to set specific parameters for the model, accepting a parameter name and a value.
    - `--record-paths`: Enables recording of paths during the computation process.
    - `--stop-when-finished`: Determines the computation step at which the script should stop, with choices constrained to steps defined in `lv.TOPOLOGY_STEP_LIST`.
    - `-z`, `--zeros`: Estimates the fixed points, which can be critical for understanding the system's behavior under various conditions.
#### Examples of Command-Line Usage

Here are some examples of how to use the command-line options to run the script:

1. **Basic Usage with Mandatory Boundary Setting**:
   ```bash
   python script_name.py output_results.out -b planetary-boundary
   ```
   This command specifies the output file and sets the boundary condition to `"planetary-boundary"`.

2. **Using Multiple Management Options and Specifying Parameters**:
   ```bash
   python script_name.py output_results.out -b both --management1 --management2 -p A_mid 500 -p W_mid 200
   ```
   This command runs the script with both planetary and social boundaries, includes two management strategies, and sets parameters `'A_mid'` and `'W_mid'` to specific values.

3. **Dry Run with Eddies and No Save**:
   ```bash
   python script_name.py output_results.out -b social-foundation -d -e -n
   ```
   This setup prepares everything for a run considering `"social-foundation"` boundaries, includes eddies in the computation, and performs a dry run without saving the results.

4. **Integration Mode with Custom Grid Points and Forced Overwrite**:
   ```bash
   python script_name.py output_results.out -b planetary-boundary -i --num 1000 -f
   ```
   This command configures the script to use integration instead of linear approximation, sets the grid to 1000 points per dimension, and forces the overwrite of the existing output file.


These examples demonstrate the flexibility of the script's command-line interface, allowing users to tailor the execution to their specific needs for detailed environmental model analysis.

- **Management Arguments**:
  - A separate group of arguments is created for management options, where each management strategy from `MANAGEMENTS` is added as an argument. This allows users to specify one or more management strategies that influence the model's computation. 

#### Implementation Details

- **Argument Group Creation**:
  - A specific group for management options is created using the `add_argument_group` method, titled "management options". This organizational step helps in segregating management-related settings from other input options, improving clarity and usability.

- **Dynamic Argument Configuration**:
  - The script dynamically generates command-line arguments for each management strategy defined in the `MANAGEMENTS` dictionary:
    - **Long Flag**: Each management option can be specified with a long flag format (`--<management_name>`), making it clear and descriptive.
    - **Short Flag**: A shorter version of the flag (`--<m>`) is also available for convenience.
  - These arguments are set up to append the management identifier to a list (`managements`) when the corresponding flag is used. This mechanism allows for the selection of multiple management strategies in a single command-line invocation.
  - The management identifiers are stored as constants (`const=m`), and each management argument defaults to an empty list (`default=[]`), ensuring that no management strategies are applied unless explicitly specified by the user.

#### Example Usage

To apply specific management strategies during the script execution, users can include one or more management flags in their command-line command. Here are a few examples:

- **Single Management Strategy**:
  ```bash
  python script_name.py --management1
  ```
  This command applies the 'management1' strategy to the model.

- **Multiple Management Strategies**:
  ```bash
  python script_name.py --management1 --management2
  ```
  This command configures the model to use both 'management1' and 'management2' strategies together.

This flexible management selection mechanism allows researchers and practitioners to explore different scenarios and their impacts on the AYS model, facilitating comprehensive studies and analyses.


- **Argument Completion**:
  - The script integrates `argcomplete` for command-line completion, enhancing user experience by providing real-time suggestions and completions based on the defined arguments.

- **Parsing**:
  - The arguments are parsed, and the results are stored in an `args` variable, which is then used throughout the script to customize the model's setup and computation according to the user's preferences.

#### 4. **Main Execution Block**

The main execution block of the script orchestrates the setup and execution of the AYS model analysis using the PyViability package. This section is crucial as it integrates user inputs and system configurations to perform the model computation. Here’s a detailed breakdown of each step and line of code within this block:

#### Initial Checks and Setup

- **Output File Suffix Check**:
  ```python
  if not args.dry_run and not args.output_file.endswith(OUTPUT_FILE_SUFFIX):
      parser.error("please use the suffix '{}' for 'output-file' (reason is actually the '.gitignore' file)".format(OUTPUT_FILE_SUFFIX))
  ```
  This conditional statement checks if the output file specified by the user ends with the predefined suffix (`.out`). If not, and if it's not a dry run, the script raises an error. This check helps maintain consistency in file naming and ensures that output files are recognized by version control configurations (like `.gitignore`).

- **Existing File Check**:
  ```python
  if not (args.force or args.dry_run):
      if os.path.isfile(args.output_file):
          parser.error("'{}' exists already, use '--force' option to overwrite".format(args.output_file))
  ```
  Before proceeding, the script checks if the output file already exists to avoid unintentional data overwriting. If the file exists and neither `--force` nor `--dry-run` flags are active, an error is raised, prompting the user to either enable the force option or choose a different file name.

#### Configuration and Model Setup

- **Grid Parameters Update**:
  ```python
  ays.grid_parameters["n0"] = args.num
  ```
  This line updates the number of points per dimension for the grid used in the model, based on user input. It ensures that the grid configuration aligns with the user’s specifications for the analysis resolution.

- **Management Strategies Display**:
  ```python
  print("managements: {}".format(", ".join(args.managements) if args.managements else "(None)"))
  ```
  The script prints out the management strategies selected by the user. This confirmation is useful for verification and ensures that the user is aware of the active configurations.

#### Parameter Modifications

- **Dynamic Parameter Setting**:
  ```python
  if args.changed_parameters:
      print("parameter changing:")
      combined_parameters = dict(ays.AYS_parameters)
      combined_parameters.update(ays.grid_parameters)
      combined_parameters.update(ays.boundary_parameters)
      for par, val in args.changed_parameters:
          for d in [ays.AYS_parameters, ays.grid_parameters, ays.boundary_parameters]:
              if par in d:
                  try:
                      val2 = eval(val, combined_parameters)
                  except BaseException as e:
                      print("couldn't evaluate {!r} for parameter '{}' because of {}: {}".format(val, par, e.__class__.__name__, str(e)))
                      sys.exit(1)
                  print("{} = {!r} <-- {}".format(par, val2, val))
                  d[ par ] = val2
                  break
          else:
              parser.error("'{}' is an unknown parameter".format(par))
  ```
  This segment allows users to modify specific model parameters through the command line. It first checks if any parameter changes are specified. If so, it attempts to update the respective dictionaries (`AYS_parameters`, `grid_parameters`, `boundary_parameters`) with the new values, evaluating expressions where necessary. Errors in evaluation are caught and reported, and an error is raised for unrecognized parameters.

#### Globalization of Parameters

- **Making Parameters Global**:
  ```python
  ays.globalize_dictionary(ays.boundary_parameters, module=ays)
  ays.globalize_dictionary(ays.grid_parameters, module=ays)
  ays.globalize_dictionary(ays.grid_parameters)
  ```
  These lines make all the parameters available globally within the `ays` module. This step is crucial for ensuring that all parts of the module have access to the latest configurations.

#### Management of Boundaries

- **Boundary Conditions Setup**:
  ```python
  if args.boundaries == "both":
      ays.AYS_sunny = ays.AYS_sunny_PB_SF
      args.boundaries = ["planetary-boundary", "social-foundation"]
  elif args.boundaries == "planetary-boundary":
      ays.AYS_sunny = ays.AYS_sunny_PB
      args.boundaries = [args.boundaries]
  elif args.boundaries == "social-foundation":
      ays.AYS_sunny = ays.AYS_sunny_SF
      args.boundaries = [args.boundaries]
  else:
      assert False, "something went wrong here ..."
  assert isinstance(args.boundaries, list) and args.boundaries
  ```
  This code configures the boundary conditions for the model based on user input. It adjusts the settings for the sunny matrix (`AYS_sunny`) and ensures that the boundaries are correctly formatted as a list. This setup is vital for the subsequent model computations that depend on these boundary settings.

Each part of the main execution block is designed to meticulously prepare the script for the computational tasks ahead, ensuring that all user inputs and configurations are correctly integrated and verified before the model computations commence.

### Detailed Execution Process with Boundary Conditions and Computation Setup

This section of the script focuses on initializing and conducting the computations for the AYS model, including setting up boundary conditions, configuring the computational grid, and handling the model's run based on the specified parameters. Here is an in-depth explanation of each part:

#### Setting Boundary Conditions

- **Planetary Boundary Condition**:
  ```python
  if "planetary-boundary" in args.boundaries:
      print("planetary / CO2 concentration:", end=" ")
      print("A_PB = {:6.2f} GtC above equ. <=> {:6.2f} ppm <=> a_PB = {:5.3f}".format(ays.A_PB, (ays.A_PB + ays.AYS_parameters["A_offset"]) / 840 * 400, ays.A_PB / (ays.A_mid + ays.A_PB)))
  ```
  This segment checks if the planetary boundary condition is included in the user's input. If so, it calculates and displays the CO2 concentration in terms of gigatons of carbon (GtC) above equilibrium, parts per million (ppm), and a normalized index. The formula adjusts the absolute values to more interpretable metrics, facilitating better understanding and communication of the boundary condition.

- **Social Foundation Boundary Condition**:
  ```python
  if "social-foundation" in args.boundaries:
      print("social foundation / welfare limit:", end=" ")
      print("W_SF = {:4.2e} US$ <=> w_SF = {:5.3f}".format(ays.W_SF, ays.W_SF / (ays.W_mid + ays.W_SF)))
  ```
  This checks for the social foundation boundary condition and, if selected, outputs the welfare limit in US dollars and a normalized value. This information helps in understanding the economic thresholds considered in the model.

#### Computational Grid Setup

- **Grid Generation**:
  ```python
  grid, scaling_vector, offset, x_step = viab.generate_grid(boundaries, n0, grid_type, verbosity=verbosity)
  ```
  The script generates a computational grid normalized to the unit interval in each dimension. The function `viab.generate_grid` takes boundary conditions, the number of grid points per dimension, grid type, and verbosity level, returning the grid and associated scaling factors necessary for the computations.

- **Step Size Configuration**:
  ```python
  lv.STEPSIZE = 2 * x_step * max([1, np.sqrt(n0 / 80)])
  print("stepsize / gridstepsize: {:<5.3f}".format(lv.STEPSIZE / x_step))
  ```
  The step size for computations is set proportional to the inverse square root of the number of grid points, ensuring finer resolution for larger grids. This step size is crucial for determining the precision and stability of the model's numerical methods.

#### Initial State Setup

- **State Array Initialization**:
  ```python
  states = np.zeros(grid.shape[:-1], dtype=np.int16)
  ```
  An array to hold the states of each grid point is initialized. This array tracks whether each point is viable, non-viable, or a shelter based on the computations.

- **Shelter Marking**:
  ```python
  states[np.linalg.norm(grid - [0, 1, 1], axis=-1) < 5 * x_step] = -lv.SHELTER
  ```
  Points within a certain distance from a specified location in the grid are marked as shelters. This setup is part of the model's boundary conditions, identifying regions in the state space that represent safe or stable configurations.

#### Model Run Functions

- **Default Run Setup**:
  ```python
  default_run = viab.make_run_function(ays.AYS_rescaled_rhs, helper.get_ordered_parameters(ays._AYS_rhs, ays.AYS_parameters), *run_args, **run_kwargs)
  ```
  A function for running the model with default settings is created. This function is configured to use the rescaled right-hand side (RHS) of the model equations and the current model parameters.

- **Management Strategy Runs**:
  ```python
  management_runs = []
  for m in args.managements:
      management_dict = ays.get_management_parameter_dict(m, ays.AYS_parameters)
      management_run = viab.make_run_function(ays.AYS_rescaled_rhs, helper.get_ordered_parameters(ays._AYS_rhs, management_dict), *run_args, **run_kwargs)
      management_runs.append(management_run)
  ```
  For each management strategy selected, a corresponding run function is created. These functions are stored in a list for use during the viability computations, allowing the model to consider different management scenarios.

#### Computation Execution and Handling

- **Computation Invocation**:
  ```python
  if not args.dry_run:
      try:
          viab.topology_classification(grid, states, [default_run], management_runs, sunny, grid_type=grid_type, compute_eddies=args.eddies, out_of_bounds=out_of_bounds, remember_paths=args.record_paths, verbosity=verbosity, stop_when_finished=args.stop_when_finished)
      except SystemExit as e:
          print("interrupted by SystemExit or Signal {} [{}]".format(ays_general.NUMBER_TO_SIGNAL[e.args[0]], e.args[0]))
  ```
  The main viability computation is executed unless a dry run is specified. The function `viab.topology_classification` is called with the prepared grid, states, run functions, and other settings. This function handles the core analysis, applying the AYS model under varying conditions and recording the results. Interruptions and signals are caught and reported for user awareness.

- **Runtime Reporting**:
  ```python
  time_passed = time.time() - start_time
  print("run time: {!s}".format(dt.timedelta(seconds=time_passed)))
  ```
  After the computations, the total runtime is calculated and displayed. This information is useful for evaluating the performance and efficiency of the model computations.

This section of the script encapsulates the core computational activities of the AYS model analysis, configuring the model environment, executing the calculations, and managing the outputs based on user-defined settings and conditions.

#### 5. **Output Handling**
The output handling section of the script is responsible for managing the results generated from the AYS model computations. This includes storing the results in a specified output file and ensuring that all relevant data is recorded accurately and efficiently. Here is a detailed breakdown of the steps involved in this process:

#### Post-Computation Data Management

- **Backscaling Grid**:
  ```python
  if args.backscaling:
      grid = viab.backscaling_grid(grid, scaling_vector, offset)
  ```
  If the `--backscaling` option is enabled, this line applies a backscaling transformation to the grid. Backscaling adjusts the grid dimensions back to their original scale after the computation. This step is crucial for interpreting the results in the context of the original model parameters and ensuring that the outputs are meaningful and usable.

- **Result Evaluation and Display**:
  ```python
  viab.print_evaluation(states)
  ```
  After the computations are complete, this function call prints an evaluation of the states determined by the viability computation. It provides a summary or detailed view of the results, facilitating immediate insight into the outcomes of the model analysis.

#### Saving Results

- **Conditional Saving**:
  ```python
  if not args.no_save:
      header = {
              "aws-version-info": __version_info__,
              "model": "AWS",
              "managements": args.managements,
              "boundaries": args.boundaries,
              "grid-parameters": ays.grid_parameters,
              "model-parameters": ays.AYS_parameters,
              "boundary-parameters": ays.boundary_parameters,
              "start-time": start_time,
              "run-time": time_passed,
              "viab-backscaling-done": args.backscaling,
              "viab-scaling-vector": scaling_vector,
              "viab-scaling-offset": offset,
              "input-args": args,
              "stepsize": lv.STEPSIZE,
              "xstep" : x_step,
              "out-of-bounds": out_of_bounds,
              "remember-paths": args.record_paths,
              "computation-status" : viab.get_computation_status(),
              }
      data = {"grid": grid,
              "states": states,
              }
      if args.record_paths:
          data["paths"] = lv.PATHS
          data["paths-lake"] = lv.PATHS_LAKE
      if not args.dry_run:
          ays_general.save_result_file(args.output_file, header, data, verbose=1)
  ```
  
  - This block checks if the `--no-save` flag is not set, indicating that the user wants to save the results. 
  - It constructs a `header` dictionary that includes metadata about the computation, such as version information, model details, parameters used, start and run times, and other relevant settings. This metadata is essential for reproducibility and understanding the context of the computation.
  - A `data` dictionary is created to store the main results (`grid` and `states`). If path recording was enabled (`--record-paths`), paths data is also included.
  - Finally, if it's not a dry run, the `save_result_file` function from the `ays_general` module is called to write the header and data to the specified output file. The function is passed a verbosity level to control the amount of output during the saving process.


The output handling section is designed to ensure that the results of the AYS model computations are managed efficiently and stored securely. It provides options to adjust the data presentation (via backscaling), review the results immediately (through state evaluation), and save all necessary information in a structured format. This approach not only secures the data but also enhances the usability and accessibility of the results for further analysis or reporting.

### Conclusion
The script is an advanced tool for conducting detailed and customizable analyses on the AYS model using the PyViability package. It supports a wide range of configurations and adjustments, making it suitable for precise scientific studies and robust model evaluations in environmental and sustainability research.