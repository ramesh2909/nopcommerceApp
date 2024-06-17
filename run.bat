python -m pytest -v -m "sanity" --html=Reports/report.html testCases/
rem python -m pytest -v -m "sanity" --html=Reports/report.html testCases/ --browser Edge
rempython -m pytest -v -m "sanity" --html=Reports/report.html testCases/ --browser Chrome
rem python -m pytest -v -m "sanity" --html=Reports/report.html testCases/ --browser Firefox
rem python -m pytest -v -m "sanity or regression" --html=Reports/report.html testCases/
rem python -m pytest -v -m "sanity and regression" --html=Reports/report.html testCases/
rem python -m pytest -v -m "regression" --html=Reports/report.html testCases/

pause

