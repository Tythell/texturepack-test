git archive -o latest.zip HEAD
gh release upload Latest latest.zip --clobber
# rm latest.zip