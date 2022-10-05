const data = [
    ['0','2022/8/23', '08:00:00', '', 'milk', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',  '', '', ''],
    ['0','2022/8/23', '08:00:00', '', 'milk', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',  '', '', ''],
    ['0','2022/8/23', '08:00:00', '', 'milk', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',  '', '', ''],
    ['0','2022/8/23', '08:00:00', '', 'milk', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',  '', '', '']
];

const container = document.getElementById('log-table');
const hot = new Handsontable(container, {
    data: data,
    // 37 columns
    colHeaders: [
        "Flag",
        "Date",
        "Time",
        "Meal type",
        "Food inputs (from client)",
        "Food inputs (breakout)",
        "Cooking method",
        "Cooking fats added (numerator)",
        "Cooking fats added (denominator)",
        "Location",
        "Portion size",
        "Portion measurement unit",
        "Photograph",
        "Food Tags (breakout)",
        "Drink inputs (from client)",
        "Drink size (numerator)",
        "Drink size (denominator)",
        "Drink inputs (breakout)",
        "Drink Tags (breakout)",
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
    columns: [
//        "Flag"
        {
            data: 0,
            type: "text"
        },
//        "Date"
        {
            data: 1,
            type: "date"
        },
//        "Time"
        {
            data: 2,
            type: "time"
        },
//        "Meal type"
        {
            data: 3,
            type: "text"
        },
//        "Food inputs (from client)"
        {
            data: 4,
            type: "text"
        },
//        "Food inputs (breakout)"
        {
            data: 5,
            type: "text"
        },
//        "Cooking method"
        {
            data: 6,
            type: "text"
        },
//        "Cooking fats added (numerator)"
        {
            data: 7,
            type: "text"
        },
//        "Cooking fats added (denominator)"
        {
            data: 8,
            type: "text"
        },
//        "Location"
        {
            data: 9,
            type: "text"
        },
//        "Portion size"
        {
            data: 10,
            type: "text"
        },
//        "Portion measurement unit"
        {
            data: 11,
            type: "text"
        },
//        "Photograph"
        {
            data: 12,
            type: "text"
        },
//        "Food Tags (breakout)"
        {
            data: 13,
            type: "text"
        },
//        "Drink inputs (from client)"
        {
            data: 14,
            type: "text"
        },
//        "Drink size (numerator)"
        {
            data: 15,
            type: "text"
        },
//        "Drink size (denominator)"
        {
            data: 16,
            type: "text"
        },
//        "Drink inputs (breakout)"
        {
            data: 17,
            type: "text"
        },
//        "Drink Tags (breakout)"
        {
            data: 18,
            type: "text"
        },
//        "Flatulence (incidental)"
        {
            data: 19,
            type: "text"
        },
//        "Flatulence (daily)"
        {
            data: 20,
            type: "text"
        },
//        "Faeces"
        {
            data: 21,
            type: "text"
        },
//        "Discomfort (incidental)"
        {
            data: 22,
            type: "text"
        },
//        "Discomfort (daily)"
        {
            data: 23,
            type: "text"
        },
//        "Discomfort descriptor"
        {
            data: 24,
            type: "text"
        },
//        "Reflux (incidental)"
        {
            data: 25,
            type: "text"
        },
//        "Reflux (daily)"
        {
            data: 26,
            type: "text"
        },
//        "Vomiting (incidental)"
        {
            data: 27,
            type: "text"
        },
//        "Vomiting (daily)"
        {
            data: 28,
            type: "text"
        },
//        "Sleep quantity"
        {
            data: 29,
            type: "text"
        },
//        "Sleep quality"
        {
            data: 30,
            type: "text"
        },
//        "Sleep notes"
        {
            data: 31,
            type: "text"
        },
//        "Mental state (mood)"
        {
            data: 32,
            type: "text"
        },
//        "Exercise (duration)"
        {
            data: 33,
            type: "text"
        },
//        "Exercise (type)"
        {
            data: 34,
            type: "text"
        },
//        "Weight"
        {
            data: 35,
            type: "numeric"
        },
//        "Ad hoc"
        {
            data: 36,
            type: "text"
        }

    ],
    rowHeaders: true, // enable the default row headers
    //colHeaders: true, // enable the default col headers
    licenseKey: 'non-commercial-and-evaluation'// for non-commercial use only
});
//
//export function starRenderer(
//  instance,
//  td,
//  row,
//  column,
//  prop,
//  value,
//  cellProperties
//) {
//  Handsontable.renderers.TextRenderer.apply(this, [
//    instance,
//    td,
//    row,
//    column,
//    prop,
//    "★".repeat(value),
//    cellProperties
//  ]);
//}

//const container2 = document.getElementById('example-table');
//const hot2 = new Handsontable(container2, {
//    data: [
//        [2,"*"],
//        [1,"*"],
//        [2,"*"],
//        [3,"*"]
//    ],
//    // test columns
//    colHeaders: [
//        "Flag"
//    ],
//    columns: [
////        "Flag"
////        {
////            data: 0,
////            renderer: starRenderer,
////            className: "star htCenter"
////        },
//        {
//            data: 0,
//            type: "numeric"
//        },
//        {
//            data: 1,
//            type: "numeric"
//        }
//    ],
//    rowHeaders: true, // enable the default row headers
//    licenseKey: 'non-commercial-and-evaluation'// for non-commercial use only
//});
//
//
