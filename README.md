# The American Union Official Website
A website I am making for the fictional American Union that has been constructed on Google Docs over the past year. Made using Flask and a good amount of other backend Python that integrades with it, as well as HTML, CSS, and JS of course. Uses JSON for the stats data. Still a work in progress!

## Current Features
- A brutalist and colorful website homepage linking to nation stats, document creator, AUTs, and DGDs (the latter two are on Google Docs)
- A nation stats page having global population, global wealth, unions, nations, and a map, with auto-updating counts. Stats for unions and nations are easily editable, including the name and background color. You can also add and delete new rows, as well as upload and download the nation map.
- A full public REST API (documented in the GitHub wiki) to view and edit nation stats directly, with GET, POST, PUT and DELETE requests, also creating backups and allowing map uploads. Data sanitizing is robust and should not allow any malformed data to get through.
- A password-protected internal endpoint that allows raw unfiltered edits.
- Part of the internal backend API for the upcoming election generator, powered by Python and Rust code.
- A few root-level static files, such as robots.txt.
- A WYSIWYG (Quill) AUT/DGD editor embedded on the site to create new documents, currently without saving.
- Last 5 changes backed up as well as monthly saves for both stats.json and the nation map.
- An index of stats.json and colony-map as well as their backups at /data.

## Planned Features
Once all in progress and high priority features are completed and the project is in a stable state, the version number will be bumped to v1.0.0.

### In Progress
- All AUTs and DGDs available on the website, being hosted in a separate GitHub repo having editing functionality. Functionality will be delivered through the GitHub API.
- An election generator to streamline the creation of DGD election files, allowing for multiple formattting styles (UCN Style, Arjun Style, Freezing Style, House, Propositions). A few more backend API files are needed in addition to power it, although most are there.

### Only Plans

#### High Priority - Ready to Start
- Undo and redo changes buttons in case something was not meant to be deleted, using buttons along with CTRL-Z and CTRL-Y.
- Saving functionality for the AUT/DGD editor, using the separate GitHub repo.
- A person lookup listing notable people from AUTs and DGDs, using descriptions from those documents as well as creating age, gender, nationality, etc.
- 

#### Low Priority - May Be Scrapped
- A login system before editing using a global password for everybody that persists forever on the device.
- Confirmation for deletion of rows in Nation Stats.
- A Union Security Market to keep track of stocks.
- A nation search bar to find countries quickly, using CTRL-F.
- More small, descriptive pages on the website in the style of the homepage
- More drama in the design of the homepage, especially regarding nukes
- Redirect/proxying from colonyhub.netlify.app and americanunion.netlify.app. Maybe also hosting on Back4App, Azure, Oracle?

## Known Bugs
- None currently!