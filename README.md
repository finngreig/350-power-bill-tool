# 350 Aotearoa's Power Bill Tool Utility Scripts

This repo contains utility scripts for 350 Aotearoa's Power Bill Tool, which compares what power bills would be based on renewable-only generation and the current generation mix.

## `generation_averages.py`

### Features

- Calculates average prices across electricity sources.
- Filters data based on the desired month and year.
- Handles JSON data format.

### Requirements

- Python 3.x

### Usage

Run the script using Python 3.x:

```bash
# python3 generation_averages.py <file> <month> <year>
$ python3 generation_averages.py prices.json 03 2023
```

The script will calculate and display the average prices across electricity sources for the specified month.

### Example Output

```
3/2023 Average for Battery: 0.00
3/2023 Average for Coal: 130.04
3/2023 Average for Cogen: 148.69
3/2023 Average for Gas: 156.05
3/2023 Average for Geothermal: 143.09
3/2023 Average for Hydro: 136.67
3/2023 Average for Diesel/Oil: 28.52
3/2023 Average for Wind: 137.77
```

## License

These utility scripts are a part of 350 Aotearoa's Power Bill Tool and are available under the MIT License. For more information, please refer to the [LICENSE](LICENSE) file.

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check the [issues](../../issues) page if you want to contribute.
