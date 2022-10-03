const data = [
    ['0','2022/8/23', '08:00:00', 'milk', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    ['2019', 10, 11, 12, 13],
    ['2020', 20, 11, 14, 13],
    ['2021', 30, 15, 12, 00]
];

const container = document.getElementById('log-table');
const hot = new Handsontable(container, {
    data: data,
    // 36 columns
    colHeaders: [
        "Flag",
        "Date",
        "Time",
        "Food Inputs (from client)",
        "Food Inputs (breakout)",
        "Cooking method",
        "Cooking fats added (numerator)",
        "Cooking fats added (denominator)",
        "Location",
        "Portion size",
        "Photograph",
        "Portion measurement unit",
        "Tags (breakout)",
        "Drink inputs (from client)",
        "Drink size (numerator)",
        "Drink size (denominator)",
        "Drink inputs (breakout)",
        "Tags (breakout)",
        "Flatulence (incidental)",
        "Flatulence (daily)",
        "Faeces",
        "Discomfort (incidental)",
        "Discomfort (daily)",
        "Discomfort descriptor",
        "Reflux (incidental)",
        "Reflux (daily)",
        "Vomiting (incidental)",
        "Vomiting (daily)",
        "Sleep quantity",
        "Sleep quality",
        "Sleep notes",
        "Mental state (mood)",
        "Exercise (duration)",
        "Exercise (type)",
        "Weight",
        "Ad hoc"
    ],
    rowHeaders: true, // enable the default row headers
    //colHeaders: true, // enable the default col headers
    licenseKey: 'non-commercial-and-evaluation'// for non-commercial use only
});