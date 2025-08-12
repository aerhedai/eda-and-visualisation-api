# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),  
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.0.0] - 2025-08-12
### Added
- Initial release of EDA and Visualisation API.
- `/eda-insights` endpoint to perform statistical summaries and dataset profiling.
- `/visualisation` endpoint to generate histograms, bar charts, and scatter plots using Plotly.
- Pydantic request/response models for validation.
- Logging configuration for API activity tracking.
- Unit tests for both endpoints.

### Notes
- This release uses Plotly for JSON chart output, allowing for easy embedding into dashboards without file I/O.
- Designed to integrate with Dataset AI pipeline tester.