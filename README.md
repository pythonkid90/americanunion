# The American Union Official Website
A website I am making for the fictional American Union that has been constructed on Google Docs over the past year. Made using Flask and a good amount of other backend Python that integrades with it, as well as HTML, CSS, and JS of course. Uses JSON for the stats data. Still a work in progress!

## Current Features
- A brutalist and colorful website homepage linking to nation stats, document creator, AUTs, and DGDs (the latter two are on Google Docs)
- A nation stats page having global population, global wealth, unions, nations, and a map, with auto-updating counts. Stats for unions and nations are easily editable, including the name and background color. You can add and delete new rows.
- A full REST API (documented in the GitHub wiki) to edit the nation stats page, with GET, POST, and DELETE requests. There is also a password-protected internal endpoint that allows raw unfiltered edits.
- Part of the internal backend API for the upcoming election generator, powered by Python and Rust code.
- A few root-level static files, such as robots.txt.
- A WYSIWYG (Quill) AUT/DGD editor embeedded on the site to create new documents, currently without saving.
- Last 5 changes backed up as well as monthly saves for stats.json.

## Planned Features

### In Progress
- All AUTs and DGDs available on the website, being hosted in a separate GitHub repo having editing functionality. Functionality will be delivered through the GitHub API.
- An election generator to streamline the creation of DGD election files, allowing for multiple formattting styles (UCN Style, Arjun Style, Freezing Style, House, Propositions). A few more backend API files are needed in addition to power it, although most are there.

### Only Plans

#### High Priority
- Undo and redo changes buttons in case something was not meant to be deleted, using buttons along with CTRL-Z and CTRL-Y.
- Saving functionality for the AUT/DGD editor, using the separate GitHub repo.
- A feature to upload new versions of the nation map, as well as being able to download the current nation map.
- Backups for the nation map (monthly as well as last 5 changes) in the same way as stats.json.
- Error detection on the nation stats page whenever the user inputs something that cannot work for a cell.
- A person lookup listing notable people from AUTs and DGDs, using descriptions from those documents as well as creating age, gender, nationality, etc.

#### Low Priority
- A login system before editing using a global password for everybody that persists forever on the device.
- A nation search bar to find countries quickly.
- More small, descriptive pages on the website in the style of the homepage
- More drama in the design of the homepage, especially regarding nukes
- Redirect/proxying from colonyhub.netlify.app and americanunion.netlify.app. Maybe also hosting on Back4App, Azure, ?

## Known Bugs
- None currently!