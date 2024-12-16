# Old books

Old books I found in auctions or antiques that I couldn't find online in a searchable form. These should all be in the public domain. Feel free to notify me if they aren't, I'll happily take them down.

## Process for adding a new book

Make sure you have a `.env` with `OPENAI_API_KEY` defined and source it.

1. Scan or download all pages
2. Iterage over them and feed them to jpg2md.py which generates a .md per page
3. Concatenate all the .md files together, cleanup, edit
4. Generate a script to produce HTML
