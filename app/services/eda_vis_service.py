import pandas as pd
import io, base64
import matplotlib.pyplot as plt
from typing import Dict, Any

def compute_eda(rows):
    df = pd.DataFrame(rows)
    # Describe all columns (numeric + categorical)
    summary = df.describe(include='all').to_dict()
    
    # Compute correlations only on numeric columns, handle empty numeric df gracefully
    numeric_df = df.select_dtypes(include=['number'])
    if numeric_df.empty:
        correlations = {}
    else:
        correlations = numeric_df.corr().to_dict()
    
    return {
        "summary": summary,
        "correlations": correlations
    }

def create_plot(rows, chart_type, x, y=None):
    df = pd.DataFrame(rows)
    plt.figure()
    if chart_type == "histogram":
        if x not in df.columns:
            raise ValueError(f"Column '{x}' not found in data for histogram.")
        df[x].hist()
    elif chart_type == "scatter":
        if y is None:
            raise ValueError("y parameter must be provided for scatter plot.")
        if x not in df.columns or y not in df.columns:
            raise ValueError(f"Columns '{x}' and/or '{y}' not found in data for scatter plot.")
        df.plot.scatter(x=x, y=y)
    else:
        raise ValueError(f"Unsupported chart type: {chart_type}")
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    plt.close()
    return base64.b64encode(buf.getvalue()).decode()
