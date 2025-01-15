// Dynamically update the current year in the footer
const currentYearSpan = document.getElementById('2025');
const currentYear = new Date().getFullYear(); // Get the current year
currentYearSpan.textContent = currentYear; // Set it to the span element

// Dynamically update the last modified date in the footer
const lastModifiedParagraph = document.getElementById('lastModified');
lastModifiedParagraph.textContent = `Last Modified: ${document.lastModified}`;

