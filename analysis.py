import marimo

__generated_with = "0.9.0"
app = marimo.App()


@app.cell
def __():
    # Email: 22f3003001@ds.study.iitm.ac.in
    # This notebook demonstrates interactive data analysis with variable dependencies
    # Cell 1: Import libraries and set up initial data
    
    import marimo as mo
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    
    # Generate sample research dataset
    np.random.seed(42)
    n_samples = 100
    
    # Create correlated variables for research analysis
    temperature = np.random.uniform(15, 35, n_samples)
    humidity = 70 - 0.8 * temperature + np.random.normal(0, 5, n_samples)
    growth_rate = 2.5 * temperature - 0.3 * humidity + np.random.normal(0, 10, n_samples)
    
    # Create DataFrame for analysis
    data = pd.DataFrame({
        'Temperature': temperature,
        'Humidity': humidity,
        'Growth_Rate': growth_rate
    })
    
    return mo, np, pd, plt, data, temperature, humidity, growth_rate, n_samples


@app.cell
def __(mo):
    # Cell 2: Interactive slider widget
    # This cell creates a temperature threshold slider
    # The slider value will be used in subsequent cells for filtering data
    
    temp_slider = mo.ui.slider(
        start=15,
        stop=35,
        step=1,
        value=25,
        label="Temperature Threshold (°C):"
    )
    
    return temp_slider,


@app.cell
def __(temp_slider):
    # Cell 3: Display slider (depends on temp_slider from Cell 2)
    # This demonstrates variable dependency between cells
    
    temp_slider
    return


@app.cell
def __(data, temp_slider, mo):
    # Cell 4: Filter data based on slider value (depends on both data and temp_slider)
    # This cell shows how data flows from Cell 1 and Cell 2
    
    threshold = temp_slider.value
    filtered_data = data[data['Temperature'] >= threshold]
    n_filtered = len(filtered_data)
    
    # Calculate statistics for filtered data
    avg_growth = filtered_data['Growth_Rate'].mean()
    avg_humidity = filtered_data['Humidity'].mean()
    
    return threshold, filtered_data, n_filtered, avg_growth, avg_humidity


@app.cell
def __(mo, n_filtered, threshold, avg_growth, avg_humidity, n_samples):
    # Cell 5: Dynamic markdown output based on widget state
    # This cell generates markdown that changes based on the slider value
    # Demonstrates dynamic content generation
    
    mo.md(f"""
    ## Data Analysis Results
    
    **Temperature Threshold:** {threshold}°C
    
    **Filtered Samples:** {n_filtered} out of {n_samples} total samples
    
    **Average Growth Rate:** {avg_growth:.2f} units
    
    **Average Humidity:** {avg_humidity:.2f}%
    
    ### Interpretation
    
    {f"⚠️ **Limited data**: Only {n_filtered} samples meet the threshold criterion." 
     if n_filtered < 20 
     else f"✓ **Sufficient data**: {n_filtered} samples available for analysis."}
    
    {f"🌡️ **High temperature conditions**: Growth rate is {avg_growth:.1f} units." 
     if threshold > 25 
     else f"🌡️ **Moderate temperature conditions**: Growth rate is {avg_growth:.1f} units."}
    """)
    return


@app.cell
def __(filtered_data, plt, threshold):
    # Cell 6: Visualization (depends on filtered_data from Cell 4)
    # Creates a scatter plot showing the relationship between variables
    # This demonstrates data flow from filtering to visualization
    
    fig, ax = plt.subplots(figsize=(10, 6))
    scatter = ax.scatter(
        filtered_data['Temperature'], 
        filtered_data['Growth_Rate'],
        c=filtered_data['Humidity'],
        cmap='viridis',
        alpha=0.6,
        s=100
    )
    
    ax.set_xlabel('Temperature (°C)', fontsize=12)
    ax.set_ylabel('Growth Rate (units)', fontsize=12)
    ax.set_title(f'Temperature vs Growth Rate (Threshold: {threshold}°C)', fontsize=14)
    ax.grid(True, alpha=0.3)
    
    cbar = plt.colorbar(scatter, ax=ax)
    cbar.set_label('Humidity (%)', fontsize=10)
    
    plt.tight_layout()
    fig
    return fig, ax, scatter, cbar


@app.cell
def __(mo):
    # Cell 7: Additional information and contact
    # Static cell with documentation
    
    mo.md("""
    ---
    ### About This Analysis
    
    This interactive notebook demonstrates:
    - **Variable Dependencies**: Cells depend on outputs from previous cells
    - **Interactive Widgets**: Slider controls data filtering
    - **Dynamic Content**: Markdown updates based on widget state
    - **Data Flow**: Clear progression from data → filtering → visualization
    
    **Author:** 22f3003001@ds.study.iitm.ac.in
    
    **Data Flow:**
    ```
    Cell 1 (data) → Cell 4 (filtered_data) → Cell 6 (visualization)
    Cell 2 (slider) → Cell 4 (threshold) → Cell 5 (markdown) & Cell 6 (plot)
    ```
    """)
    return


if __name__ == "__main__":
    app.run()
