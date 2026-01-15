# The American Union Official Website
A website I am making for the fictional American Union that has been constructed on Google Docs over the past year. Made using Flask and a good amount of other backend Python that integrades with it, as well as HTML, CSS, and JS of course. Uses JSON for the stats data. Still a work in progress!

## Current Features
- A brutalist and colorful website homepage linking to nation stats, document creator, AUTs, and DGDs (the latter two are on Google Docs)
- A nation stats page having global population, global wealth, unions, nations, and a map, with auto-updating counts. Stats for unions and nations are easily editable, including the name.

## Planned Features

### In Progress
- An AUT and DGD editor using a WYSIWYG editor (Quill) embedded on the website.
- The ability to add new unions/nations on the nation stats page
- All AUTs and DGDs moved to the website in a separate git repo having editing functionality.

### Only Plans
- An expandable column for affiliation on the nation stats page.
- A login system before editing using Flask-WTF that has logins persist for a long time.
- Error detection on the nation stats page whenever the user inputs something that cannot work for a cell.
- More drama in the design of the homepage, especially regarding nukes
- More small, descriptive pages on the website in the style of the homepage
- A person lookup listing notable people from AUTs and DGDs, using descriptions from those documents as well as creating age, gender, nationality, etc.
- An election generator to streamline the creation of DGD election files, allowing for multiple formattting styles (UCN Style, Arjun Style, Freezing Style, House, Propositions)
- A backend API to power the election generator and other small things like AUT/DGD formatting, powered by Python and Rust code.
- Redirect/proxying from colonyhub.netlify.app and americanunion.netlify.app. Maybe also hosting on Back4App?

## Known Bugs
- None currently!