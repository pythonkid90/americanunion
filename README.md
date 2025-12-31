# The American Union Official Website
A small website I made for the fictional American Union that I have constructed on Google Docs over the past year. Made using Flask and a good amount of other backend Python that integrades with it, as well as HTML, CSS, and JS of course. Uses JSON for the stats data. Still a work in progress!

## Current Features
- An unfinished website homepage linking to nation stats, AUTs, and DGDs (the latter two are on Google Docs)
- A nation stats page having unions, nations, and a map, with auto-updating counts. Stats for unions and nations are easily editable.

## Planned Features
- A login system before editing using Flask-WTF that has logins persist for a long time.
- A global population, global wealth, the ability to add new unions/nations, and maybe even an expandable column for affiliation on the nation stats page.
- Error detection on the nation stats page whenever the user inputs something that cannot work for a cell.
- A revamped and colorful homepage (maybe using typing animations for the "Keep The Peace" text) linking to other new pages on the website, such as "Our Mission".
- An AUT and DGD editor using a WYSIWYG editor embedded on the website, with all AUTs and DGDs moved to the website as well.
- A person lookup listing notable people from AUTs and DGDs, using descriptions from those documents as well as creating age, gender, nationality, etc.
- An election generator to streamline the creation of DGD election files, allowing for multiple formattting styles (UCN Style, Arjun Style, Freezing Style, House, Propositions), powered by Python or Rust code.
- Redirect/proxying from colonyhub.netlify.app and americanunion.netlify.app.