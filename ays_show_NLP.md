## Overview `ays_show.py`

This Python script provides a comprehensive visualization of trajectories within the AWS model, leveraging various options for configuration through command-line arguments. It interacts with other parts of a presumably larger codebase that includes the modules `ays_general` and `ays_model`.

### Modules and Libraries

- **`ays_general` and `ays_model`**: Imported modules.
- **Standard and Third-Party Libraries**:
  - `numpy` for numerical operations.
  - `scipy.integrate` and `scipy.optimize` for numerical integration and optimization tasks respectively.
  - `matplotlib` for plotting, with `mpl_toolkits.mplot3d` for 3D plotting capabilities.
  - `argparse` and `argcomplete` for handling and completing command-line arguments.
  - `pickle` for data serialization and deserialization.
  - `functools` for higher-order functions and operations on callable objects.

### Constants and Global Variables

- **Management Options**: `DG_BIFURCATION_END`, `DG_BIFURCATION_MIDDLE`, and `RUN_OPTIONS` manage different scenarios or strategies within the model, allowing the user to select through command-line arguments.

- **`DG_BIFURCATION_END` and `DG_BIFURCATION_MIDDLE`**:
  - These constants are string literals used to specifically denote different management scenarios or strategies within the model's conceptual framework.
  - `DG_BIFURCATION_END`: May represent a scenario where a management approach reaches its conclusive phase, perhaps signifying an extreme or terminal state in model dynamics.
  - `DG_BIFURCATION_MIDDLE`: Likely denotes an intermediate stage of a management strategy, possibly used to analyze or visualize the changes as the model transitions from one state to another under specific management conditions.
  - These bifurcation points are essential for simulating and studying the effects of different management strategies on the model's behavior over time.

- **`RUN_OPTIONS`**:
  - This list combines various operational modes or scenarios, including defaults and those defined by the constants `DG_BIFURCATION_END` and `DG_BIFURCATION_MIDDLE`. It also integrates other options that might be defined within the `aws.MANAGEMENTS` from the `ays_model` module.
  - The `RUN_OPTIONS` list is utilized in the command-line interface configurations. It allows users to select from a predefined list of scenarios or model configurations to simulate and visualize. This selection mechanism aids in enhancing user interaction, providing flexibility in modeling different environmental or sustainability scenarios.

### Main Execution Block

- Configures **command-line arguments** using `argparse` to allow dynamic adjustment of the script's behavior, such as selecting model trajectories to display or deciding whether to include boundaries in the plot.
- Based on the parsed arguments, different setup configurations are chosen, including setting initial conditions for trajectories and determining which parts of the model to visualize or analyze.
- Uses **numerical integration** (`scipy.integrate.odeint`) for computing trajectories in the model’s space.
- Uses **3D plotting** functions to visualize these trajectories, providing insights into the dynamics under different conditions or managements.
- Optionally, searches for and prints the **zeros of the model's RHS** if the `--zero` flag is set, aiding in stability analysis.
- **Boundary conditions** can be optionally added to the plots if required, enhancing the visualization’s informative value.


The script `ays_show.py` utilizes Python's `argparse` module to handle command-line arguments. This provides a user-friendly command-line interface, allowing users to configure the settings and behavior of the AWS model simulations and visualizations directly through the terminal. Below is a detailed examination of how the parser is set up and used within the script:

#### Parser Setup and Configuration

- **Initialization**:
  - The `argparse.ArgumentParser` is initialized with a description that explains the purpose of the script - to sample trajectories of the AWS model. This description is displayed when help information about the script is requested (e.g., running the script with `-h` or `--help`).

- **Adding Arguments**:
  - `option`: This argument allows users to choose between different predefined scenarios or management options. It is linked to the `RUN_OPTIONS` list, which contains the available choices. The default value is set to `aws.DEFAULT_NAME` which represents a standard or baseline scenario within the AWS model.
  - `--mode`: Users can select which parts of the model should be sampled. Possible choices are "all" or "lake", with "all" being the default. This controls the aspects of the model that are considered during the simulation, effectively focusing or broadening the scope of the analysis.
  - `--num`: This integer argument specifies the number of initial conditions to generate for the simulation, with a default of 400. Configuring the number of initial conditions allows users to control the resolution and granularity of the simulation results.

- **Optional Features**

- **`--no-boundary`**: To toggle the drawing of boundaries on the plot.
- **`--save-pic`**: To save the generated plot to a file.
- **`--zero`**: To compute and show zeros of the model's RHS.
- 
#### ArgumentComplete Integration

- The script enhances the command-line interface by integrating `argcomplete`, which provides automatic completions of command-line arguments in the terminal. This makes it easier for users to remember and type command-line options quickly.

#### Parsing and Handling

- After configuring all the arguments and their options, the parser concludes by calling `parser.parse_args()` to parse the command-line inputs provided by the user.
- The results are stored in an `args` object, which is then used throughout the script to customize and control the flow of data processing, modeling, and visualization according to the user’s specifications.


### Execution Flow

1. Parses and processes command-line arguments.
2. Randomly generates initial conditions if not provided through command-line.
3. Configures plot settings and model parameters based on chosen options.
4. Computes trajectories using numerical methods.
5. Plots results in a 3D space, applying color codes based on certain conditions.
6. Optionally adds model boundaries and saves the plot to an external file.

### Usage Example

Here is an example of how to run the script from a command line:
```bash
python ays_show.py --mode lake --num 200 --save-pic example.png
```
This command sets the mode to 'lake', uses 200 initial conditions, and saves the resulting plot to 'example.png'.

#### 1. Running the Default Scenario

```bash
python ays_show.py
```
- This example runs the script with default settings: using the default management scenario, plotting all parts of the model, and not saving the output to a file.

#### 2. Specifying a Management Option

```bash
python ays_show.py --option DG_BIFURCATION_MIDDLE
```
- Runs the model using the `DG_BIFURCATION_MIDDLE` management scenario. This might represent a specific setup or strategy within the model, altering how the system behaves or is visualized.

#### 3. Changing the Model Sampled Part

```bash
python ays_show.py --mode lake
```
- Samples only the 'lake' part of the model. This is useful for focusing on specific dynamics or regions within the model’s conceptual space.

#### 4. Setting the Number of Initial Conditions

```bash
python ays_show.py --num 1000
```
- Increases the number of initial conditions to 1000 for the simulation. This higher number might improve the resolution and detail of the simulation, useful in studies requiring finer granularity.

#### 5. Disabling Boundary Visualization

```bash
python ays_show.py --no-boundary
```
- Runs the simulation without drawing boundaries, which can simplify the output plot if boundaries are not of interest or relevant to the analysis.

#### 6. Saving the Output to a File

```bash
python ays_show.py --save-pic output.png
```
- Saves the visualization plot to 'output.png'. This option is essential for documenting results or using the outputs in presentations or reports.

#### 7. Computing Zero Points of RHS

```bash
python ays_show.py --zero
```
- Computes and displays zero points of the model's right-hand side in the S=0 plane, providing important insights into the stability of the model under the selected settings.

#### 8. Combining Multiple Options

```bash
python ays_show.py --option DG_BIFURCATION_END --mode all --num 500 --save-pic final_plot.png --zero
```
- In this advanced example, the script is run with the `DG_BIFURCATION_END` management scenario, using 'all' parts of the model, with 500 initial conditions, saving the plot to 'final_plot.png,' and also computing zero points for stability analysis.

These examples demonstrate how command-line arguments can be used to tailor the script’s execution to fit various needs and applications. By mixing and matching these options, users can adapt the model simulations to a wide range of scenarios, management strategies, and research questions, efficiently exploring the dynamics and outcomes of the AWS model.


Overall, `ays_show.py` serves as a crucial tool for deeply understanding and visualizing the different dynamics and outcomes possible within the AWS model according to various scenarios or management strategies.