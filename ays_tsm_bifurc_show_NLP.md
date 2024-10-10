## Overview: `ays_tsm_bifurc_show.py`

The `ays_tsm_bifurc_show.py` script is designed to visualize the results of bifurcation analyses from the AWS model. It efficiently handles command-line inputs, reads and validates data files, processes the data, and visualizes the results through detailed plots. Below is a step-by-step explanation of the script's components and functionalities:

### Imports
- **Modules for System Functionality and Data Handling**:
  - `pyviability` for viability-specific operations.
  - `numpy` for numerical operations and array handling.
  - `matplotlib.pyplot` for creating visual plots.
  - `argparse` and `argcomplete` for parsing and auto-completing command-line arguments.
  - Other standard libraries for date handling, file operations, and functional programming.

### Constants
- **`TRANSLATION`**:
  - A dictionary that maps parameter names to their formatted string representations, improving plot readability. The `TRANSLATION` dictionary in the `ays_tsm_bifurc_show.py` script plays a crucial role in enhancing the readability and presentation of the graphical outputs. This dictionary maps specific technical parameter names, which are typically used in the model's internal computations, to more readable and formatted string representations suitable for display on plots. Here's a breakdown of its structure and functionality:

#### Purpose
- **Enhance Readability**: Converts cryptic or shorthand parameter names into fully formatted and descriptive labels using LaTeX syntax. This helps in making the plots more understandable to users who may not be familiar with the shorthand notations.
- **Standardization**: Ensures consistent naming and presentation style across different plots and figures generated using this script.

#### Structure
- **Key-Value Pairs**: Each entry in the dictionary consists of:
  - **Key**: The shorthand or code-friendly parameter name used internally within the model.
  - **Value**: A LaTeX-formatted string that describes the parameter in a more detailed and visually appealing way. This formatting includes mathematical symbols and units, enhancing the scientific presentation.

#### Example Entries from `TRANSLATION`
- `"beta_DG"`: Translated to `r"$\beta_{0,LG}\, \left[\frac{\%}{\mathrm{a}}\right]$"` which represents a rate parameter, formatted to include subscripts and units of percentage per year.
- `"phi_CCS"`: Translated to `r"$\phi_{CCS}\, \left[\frac{\mathrm{GJ}}{\mathrm{GtC}}\right]$"` indicating a conversion factor with units in GigaJoules per GigaTon of Carbon.
- `"theta_SRM"` and `"sigma_ET"`: Similarly formatted to represent other specific parameters with appropriate units and mathematical notations.

#### Usage in Plotting
- **Labeling Axes and Legends**: The translated strings are used as labels for axes or in legends, wherever these parameters are referenced. This automatic replacement ensures that all occurrences of the parameter names in the visual output are replaced with their more descriptive versions.
- **Dynamic Replacement**: When generating plots, the script checks this dictionary to replace parameter names dynamically, ensuring that every instance where a parameter is mentioned, it appears in its translated form.

In summary, the `TRANSLATION` dictionary serves as a bridge between the technical parameter names used in computational models and the more descriptive, formatted labels preferred in visual presentations, thereby enhancing the accessibility and professionalism of the generated plots.


### Command-line Interface (CLI) Setup
- **Argument Parsing**:
  - Configures necessary command-line arguments to specify the bifurcation parameter, input files, verbosity level, and an option to save the resulting plot. Argument parsing in the `ays_tsm_bifurc_show.py` script is implemented using Python's `argparse` module, which provides a way to handle command-line arguments. By defining how the script should interpret the command line inputs, it allows users to customize the execution of the script according to their needs without modifying the code. Below is the detailed breakdown of how argument parsing is structured and utilized in this script:

#### Purpose
- **Customization**: Enables users to specify input parameters like the bifurcation parameter, input files, and options directly via the command line.
- **Flexibility**: Allows for optional arguments that modify the script's behavior, such as verbosity levels and saving outputs.

#### Setup
- **Parser Creation**: An instance of `argparse.ArgumentParser` is created, which serves as the foundation for building the command-line interface.
- **Argument Configuration**:
  - **Mandatory Arguments**:
    - `parameter`: The bifurcation parameter's name which is expected to change and potentially cause a bifurcation in the system. This argument is crucial for the script to know which parameter to focus on during analysis.
    - `input_files`: One or more files provided as input containing the data needed for the bifurcation analysis. These files should contain results from the TSM analysis of the AWS model.
  - **Optional Arguments**:
    - `--save-pic`: Allows specifying a file path to save the generated plot. If not provided, the plot will not be saved to a file.
    - `--verbose` (`-v`): A flag that can be used to increase the verbosity level of the output. This is useful for debugging or understanding more about the script's internal processes. It can be specified multiple times (e.g., `-v`, `-vv`) to increase the detail of debug information.

#### Usage Example
```bash
python ays_tsm_bifurc_show.py beta_DG datafile1.pkl datafile2.pkl --save-pic output.png -v
```
- This command runs the script for the bifurcation parameter `beta_DG` using `datafile1.pkl` and `datafile2.pkl` as inputs, saves the resulting plot to `output.png`, and increases the verbosity level for more detailed output.

**Basic Execution with Single Input File**
   ```bash
   python ays_tsm_bifurc_show.py theta_SRM single_datafile.pkl
   ```
   - This command runs the script focusing on the bifurcation parameter `theta_SRM` using `single_datafile.pkl` as the input. No plot is saved, and the script operates with default verbosity.

**Multiple Input Files without Saving**
   ```bash
   python ays_tsm_bifurc_show.py phi_CCS datafile1.pkl datafile2.pkl datafile3.pkl
   ```
   - This command uses three input files for the bifurcation analysis with the parameter `phi_CCS`. The output is displayed on-screen, and no file is saved.

**Saving Output to a Specific Directory**
   ```bash
   python ays_tsm_bifurc_show.py sigma_ET datafile1.pkl --save-pic results/plot_sigma_ET.png
   ```
   - This command processes the bifurcation parameter `sigma_ET` from `datafile1.pkl`, saving the generated plot to the `results/plot_sigma_ET.png`. It helps organize output files by specifying a directory.

**High Verbosity for Debugging**
   ```bash
   python ays_tsm_bifurc_show.py beta_DG datafile.pkl -vvv
   ```
   - This command analyzes the bifurcation parameter `beta_DG` using `datafile.pkl` and sets the verbosity level to very high (`-vvv`) to provide extensive debug information, useful for troubleshooting or understanding the script's behavior in detail.

**Using Auto-Completion for Argument Values**
   ```bash
   python ays_tsm_bifurc_show.py sigma_ET datafile1.pkl datafile2.pkl --save-pic output.svg -vv
   ```
   - Utilizing the `argcomplete` integration, this command allows for easier specification of arguments through tab-completion, running the script with two input files for `sigma_ET`, saving the plot as an SVG file, and providing verbose output.

### File and Data Validation
- **File Existence Check**:
  - Verifies that the specified input files exist before attempting to load them, ensuring the process does not fail due to missing files.
  - 
### Data Processing and Visualization
- **Data Validation and Loading**:
  - Validates the existence of input files.
  - Loads data files using a standardized format, ensuring compatibility and correctness of data structure with predefined headers.

- **Parameter Consistency Verification (`cmp_list`)**:
  - **Purpose**:
    - The `cmp_list` contains keys that are critical for ensuring that the headers of input data files are consistent across multiple datasets. This verification is vital for maintaining the reliability of the bifurcation analysis by ensuring that all datasets are comparable in terms of their foundational parameters.
    
  - **Components of `cmp_list`**:
    - **`model-parameters`**: Ensures that the model configurations are identical across datasets.
    - **`grid-parameters`**: Verifies that the computational grids used for simulations are consistent, which is crucial for spatial and temporal resolution matching.
    - **`boundary-parameters`**: Checks for consistency in the parameters that define the boundaries of the model, which can affect the results significantly if they differ.
    - **`managements`**: Confirms that the management or operational strategies applied in the simulations are the same, as different strategies could lead to incomparable results.

  - **Usage in the Script**:
    - The script uses `cmp_list` to compare the specified categories in the headers of all input files. If discrepancies are found in these critical parameters, the script raises an error or warning, prompting the user to check the data files. This step is performed before proceeding with any data processing or visualization to ensure that the analysis is based on a consistent and reliable dataset.

  - **Integration with `recursive_difference` Function**:
    - To implement the comparisons, the script leverages the `recursive_difference` function, a robust tool designed to identify differences between potentially nested dictionaries. This function is crucial in handling the complex structures often found in model configurations, grid settings, and other parameters stored in the headers.
    - **Example of Discrepancy Handling Using `recursive_difference`**:
      ```python
      for el in cmp_list:
          differences = ays_general.recursive_difference(reference_header[el], header[el])
          if differences:
              raise ValueError(f"Incompatible headers due to differing {el}: {differences}")
      ```
      - In this example, the script iterates through each element specified in `cmp_list`, using the `recursive_difference` function to compare the corresponding sections of the reference header and the current file's header. If the function returns any differences, it indicates that the files are not compatible for a combined analysis. The script then raises a `ValueError` with a message specifying which part of the header is incompatible and detailing the differences.

- **Data Comparison**:
  - Compares headers from different input files to ensure consistency across data sets, crucial for accurate bifurcation analysis.

- **Plot Construction**:
  - Initializes a matplotlib figure and axes, setting appropriate sizes and layout.
- **Data Processing for Plotting**:
  - Organizes and processes data to represent volumes of different regions in the phase space as a function of the bifurcation parameter.
- **Stylized Plotting**:
  - Uses filled areas between lines in the plot to represent data volumes, enhancing visual clarity and differentiation between regions.
  
### Plot Construction
The plot construction process in the `ays_tsm_bifurc_show.py` script is a crucial stage where the data prepared in previous steps is visualized in a structured and informative manner. This section of the script deals with initializing the plot environment, setting up the axes, and defining how the data will be presented graphically. Below is a detailed breakdown of each aspect involved in constructing the plot:

#### Figure and Axes Initialization
- **Figure Creation**:
  - A new figure is created using `matplotlib.pyplot.figure()`, which acts as a container for all plot elements. The size of the figure is specified to ensure that the plot has adequate space to display all elements clearly without overcrowding.
  - Example: `fig = plt.figure(figsize=(8, 9), tight_layout=True)` sets up an 8x9 inch figure with tight layout options to optimize spacing between plot elements.

- **Axes Setup**:
  - An axes object is added to the figure, which provides a context in which data can be plotted. The axes define the coordinate system and contain most of the figure elements: gridlines, tick marks, labels, etc.
  - Example: `ax = fig.add_subplot(111)` adds a subplot to the figure where `111` indicates a single subplot grid.

#### Data Organization for Plotting
- **Sorting and Structuring**:
  - Data related to the bifurcation parameter and the volumes of different regions in phase space are sorted and structured for plotting. This often involves ordering the data points according to the bifurcation parameter values and calculating intermediary points to make the plot smoother and more readable.
  - Example: The script sorts the bifurcation parameters and uses functions like `add_middles` to interpolate additional points for a smoother transition in the plotted lines.The function `add_middles` in the `ays_tsm_bifurc_show.py` script plays a crucial role in enhancing the visualization of the bifurcation analysis by interpolating additional data points between the existing points. This process smoothens the transitions in the plotted lines, making the visual representation more continuous and easier to interpret. Below is a detailed explanation of the `add_middles` function, its purpose, methodology, and its impact on the plot:

### Purpose of `add_middles`
- **Enhancing Plot Continuity**: By adding intermediate points between the existing data points, the function ensures that the plot does not have sharp jumps or breaks, which can be visually misleading or harder to follow. This is particularly important in bifurcation plots where smooth transitions indicate the behavior of the system under gradual parameter changes.
- **Visual Clarity**: Smoother lines in the plot help in better demonstrating the trends and shifts in the system's dynamics as the bifurcation parameter changes. It makes it easier for viewers to track changes and understand the underlying phenomena.

### Methodology
- **Array Manipulation**:
  - The function takes an array of sorted bifurcation parameter values and effectively triples the length of this array by inserting two additional points between each original pair of consecutive points. 
  - This is achieved using `numpy` operations where the original array is repeated and intermediate values are calculated as the mean of pairs of original points.

- **Interpolation**:
  - For each pair of original data points, the function calculates their midpoint and places this value between them. This interpolation creates a smoother transition by filling gaps that would otherwise appear as steep jumps in the plot.
  - The interpolation is not merely linear; it also checks for significant changes that might indicate a bifurcation event. If a potential bifurcation is detected based on a specified threshold (`bifurc_val`), the function adjusts the interpolated values to highlight this event more clearly.

- **Conditional Checks for Bifurcation**:
  - The function includes an optional parameter `check_bifurc` that triggers additional logic to handle potential bifurcations. If `check_bifurc` is `True`, the function scrutinizes the differences between consecutive points to detect substantial changes that surpass the `bifurc_val` threshold.
  - When such changes are detected, the function ensures that the interpolated points reflect this bifurcation by not smoothing over it excessively, thus maintaining the plot's integrity in representing critical transitions in the system's dynamics.

### Example of Function Operation
```python
def add_middles(arr, check_bifurc=False):
    new_arr = np.repeat(arr, 3)[:-2]
    new_arr[1::3] = 0.5 * (arr[:-1] + arr[1:])
    new_arr[2::3] = 0.5 * (arr[:-1] + arr[1:])
    if check_bifurc:
        for i in range(len(arr) - 1):
            i_next = i+1
            if (arr[i] > bifurc_val and arr[i_next] < bifurc_val) or (arr[i] < bifurc_val and arr[i_next] > bifurc_val):
                new_arr[1::3][i] = arr[i]
                new_arr[2::3][i] = arr[i_next]
    return new_arr
```

### Impact on the Plot
- **Smoothness and Accuracy**: The `add_middles` function ensures that the plot not only appears smoother but also accurately represents the underlying data without oversimplifying critical transitions. This balance between visual appeal and data integrity is crucial for effective data presentation.
- **Highlighting Key Changes**: By adjusting how midpoints are calculated especially near potential bifurcations, the function helps in emphasizing where significant shifts occur in the system's behavior, which is a key aspect of bifurcation analysis.


#### Stylized Plotting Techniques
- **Filled Area Plotting**:
  - The script uses `ax.fill_between()` to create filled areas between lines in the plot. This method is particularly effective for showing volumes as it clearly delineates the space occupied by each region under different conditions of the bifurcation parameter.
  - Colors and styles are set for each region to differentiate them visually. Edge colors and line widths might also be adjusted for better visibility.
  - Example: `ax.fill_between(bifurcation_parameter_list, y_before, y_now, facecolor=color, lw=2, edgecolor="white")` fills the area between `y_before` and `y_now` with the specified `facecolor` and `edgecolor`.

### Dynamic Labeling and Annotations
- **Applying Labels**:
  - Labels for the axes are set based on the bifurcation parameter and other variables. If a translation for the label exists in the `TRANSLATION` dictionary, it is used to provide a more readable and formatted label.
  - Example: `ax.set_xlabel(TRANSLATION.get(bifurcation_parameter, bifurcation_parameter))` uses a translated label if available, otherwise defaults to the raw parameter name.

- **Annotations**:
- 
  - The script may include annotations to highlight specific points, thresholds, or features on the plot. These annotations can guide the viewer's attention to important aspects or results within the data.
  
   Applies dynamic labels from the `TRANSLATION` dictionary to axis labels and annotations, improving plot readability.

- **Custom Annotations**:
  - Annotates specific points and areas on the plot to highlight important features or results, such as bifurcation points or significant changes in data behavior.
   

- The `text_xvals` dictionary in the `ays_tsm_bifurc_show.py` script serves a specific and valuable purpose in the context of annotating plots, particularly those associated with bifurcation analysis. This dictionary is used to manage and assign specific x-axis values for text annotations, ensuring that these annotations are placed optimally relative to significant points or features in the plot. Below is a detailed discussion of the purpose, structure, and usage of the `text_xvals` dictionary:

### Purpose of `text_xvals`
- **Customized Annotation Placement**: The primary function of the `text_xvals` dictionary is to provide predefined x-values for placing text annotations on the plot. These values are specifically chosen based on the bifurcation parameter to ensure that annotations are visible and do not overlap with other plot elements, enhancing readability and effectiveness.
- **Context-Sensitive Labeling**: By tailoring the x-values for annotations according to different bifurcation parameters, the script can adapt the plot's labeling dynamically to different scenarios, ensuring that the annotations always appear in contextually appropriate positions.

### Structure of `text_xvals`
- **Key-Value Pairs**: Each entry in the dictionary consists of:
  - **Key**: The name of a bifurcation parameter. This key corresponds to the parameters that might be analyzed in the bifurcation study.
  - **Value**: A numerical value representing the x-coordinate at which to place text annotations when the corresponding bifurcation parameter is being analyzed.
  
### Detailed Entries in `text_xvals`
- **`beta_DG`**: 
  - **Value**: `2.3`
  - **Rationale**: This value is chosen because it represents a position on the x-axis where significant changes in the data are observed. It is also a point where there is enough space on the plot to place clear annotations without overlapping other visual elements.
  
- **`phi_CCS`**: 
  - **Value**: `5.4e10`
  - **Rationale**: Selected based on the scale and typical data range of this parameter. This positioning ensures that annotations do not clutter the plot or overlap with critical data points, maintaining clarity.

- **`theta_SRM`**: 
  - **Value**: `6e-5`
  - **Rationale**: Chosen to align with key transitions or features specific to this parameter’s impact on the system, aiding in highlighting crucial dynamics at this scale.

- **`sigma_ET`**: 
  - **Value**: `5e12`
  - **Rationale**: Positioned to best represent the parameter’s effects within the typical range of values observed in the data, ensuring annotations are placed where they can be most informative and least intrusive.

Each of these entries is tailored to fit the scale and nature of changes observed in the plot for each parameter, reflecting thoughtful consideration of data visualization best practices. This customization enhances the plot’s utility as a tool for interpreting complex dynamical behaviors in bifurcation analysis.

### Usage in the Script
- **Dynamic Retrieval and Application**:
  - When plotting annotations, the script first checks if the current bifurcation parameter is a key in the `text_xvals` dictionary.
  - If a corresponding entry exists, the script uses the associated value as the x-coordinate for placing text annotations. This ensures that annotations are always positioned optimally for visibility and contextual relevance.
  - If no entry exists for the current parameter, the script may use a default method, such as positioning annotations at the midpoint of the plotted x-range or another heuristic.

- **Integration with Plotting Logic**:
  - The x-values from `text_xvals` are used in calls to `ax.text()`, which places text annotations on the plot. This method takes coordinates and the text string as arguments, allowing for precise control over where annotations appear.
  - Example usage:
    ```python
    text_val = text_xvals.get(bifurcation_parameter, (bifurcation_parameter_list[0] + bifurcation_parameter_list[-1]) / 2)
    ax.text(text_val, specific_y_position, "Annotation Text")
    ```
    In this example, `text_val` is dynamically determined based on the bifurcation parameter. If the parameter is not in `text_xvals`, a default position (the midpoint of the x-range) is used.

### Impact on the Plot
- **Enhanced Clarity and Readability**: By controlling the placement of text annotations through `text_xvals`, the script ensures that important labels and notes are both visible and positioned in a way that does not obscure the data. This enhances the overall clarity and effectiveness of the plot.
- **Adaptability**: The use of a dictionary to manage annotation positions allows for easy adjustments and extensions. Additional parameters can be added to `text_xvals` as needed, with values tailored to new datasets or different aspects of the model being analyzed.

Overall, the `text_xvals` dictionary is a crucial component of the plotting functionality in the `ays_tsm_bifurc_show.py` script, providing a systematic and adaptable way to manage the placement of annotations in a data-driven and context-sensitive manner. This enhances the utility and readability of bifurcation plots, making them more informative and easier to interpret.



  - Example: `ax.text(text_val, position_y, label)` places text annotations at specified positions on the plot, where `text_val` is the x-coordinate, `position_y` is the y-coordinate, and `label` is the text to display.

### Output Handling
- **Conditional Saving**:
  - If a save path is provided through the command-line arguments, the plot is saved to a file using `fig.savefig()`. This allows users to easily store, share, or publish the generated plots.
  - Example: `if args.save_pic: fig.savefig(args.save_pic)` checks if a save path is provided and saves the plot accordingly.

- **Displaying the Plot**:
  - Finally, the plot is displayed to the user using `plt.show()`. This function call brings up a window with the plot, allowing the user to inspect the visual results immediately.
  - This step is crucial for interactive sessions or when immediate feedback is required.


 
### Output Handling
- **Conditional Saving**:
  - Optionally saves the generated plot to a file if the `--save-pic` argument is provided, allowing for easy distribution or publication of results.
- **Plot Display**:
  - Displays the plot on the screen, enabling immediate visual feedback and analysis.
  
### Example Usage Scenarios
**Exploratory Analysis with Multiple Files**
   ```bash
   python ays_tsm_bifurc_show.py phi_CCS datafile1.pkl datafile2.pkl --verbose
   ```
   - This command runs the script with increased verbosity for detailed output, using two data files for the bifurcation parameter `phi_CCS`. Helps in exploring data differences and similarities in a detailed manner.

**Batch Processing for Comparative Analysis**
   ```bash
   python ays_tsm_bifurc_show.py beta_DG batch_data*.pkl --save-pic batch_comparison.png
   ```
   - Uses a glob pattern to specify multiple input files, processing all matching files in one batch. Saves the comparative plot to visualize differences or trends across multiple datasets.

This script is integral for researchers and analysts working with the AWS model, providing a robust tool for examining how changes in parameters can influence system dynamics and stability.