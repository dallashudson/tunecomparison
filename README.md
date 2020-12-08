# tunecomparison
For comparing different tunes differences from WinOLS!


How to use:
1. In WinOLS import a stock hexdump/file for either lets say an ECU, TCU, or CPC.
2. Still in WinOLS, import a tuned version of the file you just previously imported
3. Next, go in WinOLS and press View->Differences->Differences
4. A sidebar or window should open up displaying every address that has changed from file to file, press CTRL+A to select, then CTRL+C to copy
5. Next in windows somewhere you should make a text (.txt) file, and hit paste/CTRL+V into this. The format should look the same as it did in winols
6. Save this file as a .txt, the name doesn't matter
7. Repeat 1-6 for another tune so that you have two files showing the differences between a stock and tuned file
8. Open the tune comparison tool, select both txts you just made, feel free to add a comment that you can see in the result file, select a destination, and generate a report
9. Go and open the report wherever you saved it, the file should be separated into changes in both tunes, changes specific to one tune, and changes specific to the other tune.
