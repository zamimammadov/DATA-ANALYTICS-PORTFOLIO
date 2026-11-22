# Men's T20 World Cup scorecards, 2022

Who scored the most runs and who took the most wickets in the Australia tournament? This analysis covers the first round, Super 12 and knockout stages. It rebuilds player appearances from the archived scorecards and calculates tournament rates from runs and balls.

| Player | Team | Tournament result |
|---|---|---|
| Virat Kohli | India | 296 runs from 217 balls across six batting innings, a strike rate of 136.41. |
| Suryakumar Yadav | India | 239 runs from 126 balls. Third by runs and the fastest scorer among the three leading run totals, with a strike rate of 189.68. |
| Wanindu Hasaranga de Silva | Sri Lanka | 15 wickets and 199 runs conceded in 186 legal balls (31 overs), an economy of 6.42. |

## Reproduce the analysis

From this project directory, use Python 3.10+ and pandas. The command reads the checked-in JSON files and prints both leaderboards. The optional output path writes four CSV tables; choose a new directory to compare them with the committed snapshot.

```sh
python -m pip install -r requirements.txt
python scorecards.py
python scorecards.py --output build/model
python -m unittest discover -s tests
```

The [notebook](Data_preprocessing_Python.ipynb) walks through preprocessing, match coverage and both leaderboards. Open it with a Jupyter kernel using the same Python environment. [Scorecard transformations and ranking formulas](scorecards.py) · [Ready-to-query model](data/model)

## Model and coverage

- **Matches.** The match dimension includes 45 fixtures. Three abandoned matches have no innings rows. One no-result match has recorded play and contributes to player totals. Overall, 42 fixtures contribute 699 batting appearances and 500 bowling appearances.
- **Players.** The exports contain 219 profile rows. Removing captain and wicketkeeper marks yields 213 distinct team/player pairs. Batting and bowling appearances use this same two-column key; use it when joining to player profiles.
- **Match links.** The raw innings list the two teams and have no scorecard ID. The transformation checks that each pair identifies one fixture in this tournament before mapping both team orders to the same match ID. A competition with repeat fixtures would need another identifier, such as a date or scorecard URL.
- **Rates.** Batting strike rate is 100 × total runs / total balls faced. Bowling economy is 6 × runs conceded / legal balls. An entry of `3.2` overs means 20 legal balls. Zero-ball denominators give an unavailable rate. Ranking by runs or wickets favours players whose teams played more matches.

## Sources

The [archived JSON](data/raw) records the ESPNcricinfo scorecards and player profiles used in the original project. The supplemental CSV preserves the original export's optional image links and alternate biographies. The [Bright Data collector snippets](collectors) contain separate interaction and parser stages for the original selectors. The analysis runs offline using the archived data. [ESPNcricinfo tournament record](https://stats.espncricinfo.com/ci/engine/records/team/match_results.html?id=14450;type=tournament)
