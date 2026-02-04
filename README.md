# The American Union Official Website
A website I am making for the fictional American Union that has been constructed on Google Docs over the past year. Made using Flask and a good amount of other backend Python that integrades with it, as well as HTML, CSS, and JS of course. Uses JSON for the stats data. Still a work in progress!

## Current Features
- A brutalist and colorful website homepage linking to nation stats, document creator, AUTs, and DGDs (the latter two are on Google Docs)
- A nation stats page having global population, global wealth, unions, nations, and a map, with auto-updating counts. Stats for unions and nations are easily editable, including the name and background color. You can add and delete new rows.
- A full REST API (documented in the GitHub wiki) to edit the nation stats page, with GET, POST, and DELETE requests.
- An internal API with many election tools in both Python and Rust.
- A few root-level static files, such as robots.txt.

## Planned Features

### In Progress
- An AUT and DGD editor using a WYSIWYG editor (Quill) embedded on the website. Currently the Quill editor is there but there is no saving functionality.
- All AUTs and DGDs available on the website, being hosted in a separate GitHub repo having editing functionality. Functionality will be delivered through the GitHub API.
- An election generator to streamline the creation of DGD election files, allowing for multiple formattting styles (UCN Style, Arjun Style, Freezing Style, House, Propositions). Many of the election files are already available in the internal API (not the REST API), although progress has not started on integrating them into the site.

### Only Plans
- A feature to upload new versions of the nation map, as well as being able to download the current nation map.
- A login system before editing using a global password for everybody that persists forever on the device.
- Error detection on the nation stats page whenever the user inputs something that cannot work for a cell.
- More drama in the design of the homepage, especially regarding nukes
- More small, descriptive pages on the website in the style of the homepage
- A person lookup listing notable people from AUTs and DGDs, using descriptions from those documents as well as creating age, gender, nationality, etc.
- A backend API to power the election generator and other small things like AUT/DGD formatting, powered by Python and Rust code.
- Redirect/proxying from colonyhub.netlify.app and americanunion.netlify.app. Maybe also hosting on Back4App?
- Backups every month for stats.json and the nation map, also with the 5 most recent stats and maps always backed up, possibily in Git/GitHub rather than volumes.

## Known Bugs
- None currently!