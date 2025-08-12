import pandas as pd
import io, base64
import matplotlib.pyplot as plt
from typing import Dict, Any

def compute_eda(rows):
    df = pd.DataFrame(rows)
    return {
        "summary": df.describe(include='all').to_dict(),
        "correlations": df.corr().to_dict()
    }

def create_plot(rows, chart_type, x, y=None):
    df = pd.DataFrame(rows)
    plt.figure()
    if chart_type == "histogram":
        df[x].hist()
    elif chart_type == "scatter" and y:
        df.plot.scatter(x=x, y=y)
    else:
        raise ValueError("Unsupported chart")
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    plt.close()
    return base64.b64encode(buf.getvalue()).decode()
