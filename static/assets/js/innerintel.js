
console.log('--- table ---');

const data = [];
var changes_list = [];

function updateLog() {
    console.log("+++++ update logs +++++");
    console.log("+++++ changes_list.length: "+changes_list.length);

    var httpRequest = new XMLHttpRequest();
    httpRequest.open('POST', '', true);
    httpRequest.setRequestHeader("Content-type","application/x-www-form-urlencoded");
    console.log(JSON.stringify(changes_list));
    httpRequest.send('changes_list='+JSON.stringify(changes_list));
    /**
     * After getting the data
     */
    httpRequest.onreadystatechange = function () {
        if (httpRequest.readyState == 4 && httpRequest.status == 200) {
            console.log("httpRequest.status == 200");
            changes_list = [];
            alert("Update success!");
        }
        else
            alert("Update failed, please try again!");
    };
};

for(i in logs){
    var log = logs[i]
    var obj = [
        log.lid,
        log.flag,
        log.date,
        log.time,
        log.meal_type,
        log.client_food_input,
        log.client_food_break_out,
        log.cooking_method,
        log.cooking_fats_added_numerator,
        log.cooking_fats_added_denominator,
        log.location,
        log.portion_size,
        log.portion_measurement_unit,
        log.photograph,
        log.food_tags_breakout,
        log.client_drink_input,
        log.drink_size_numerator,
        log.drink_size_denominator,
        log.drink_input_breakout,
        log.drink_tags_breakout,
        log.flatulence_incidental,
        log.flatulence_daily,
        log.faeces,
        log.discomfort_incidental,
        log.discomfort_daily,
        log.discomfort_descriptor,
        log.reflux_incidental,
        log.reflux_daily,
        log.vomiting_incidental,
        log.vomiting_daily,
        log.sleep_quantity,
        log.sleep_quality,
        log.sleep_notes,
        log.mental_state_mood,
        log.exercise_duration,
        log.exercise_type,
        log.weight,
        log.ad_hoc
    ];
    for(var j=0;j<obj.length;j++){
        if (obj[j] == '""'){
            obj[j] = '';
        }
    }
    data.push(obj);
}


const container = document.getElementById('log-table');
const hot = new Handsontable(container, {
    afterChange: function(changes, source) {
            if(changes != null) {
                var row_index = changes[0][0];
                var col_index = changes[0][1];
                var rowdata = hot.getDataAtRow(row_index);
                console.info("update row_index: "+row_index);
                console.info("update col_index: "+col_index);
                console.info("update row: "+hot.getDataAtRow(row_index));
                const log = {
                    'lid':rowdata[0],
                    'flag':rowdata[1],
                    'date':rowdata[2],
                    'time':rowdata[3],
                    'meal_type':rowdata[4],
                    'client_food_input':rowdata[5],
                    'client_food_break_out':rowdata[6],
                    'cooking_method':rowdata[7],
                    'cooking_fats_added_numerator':rowdata[8],
                    'cooking_fats_added_denominator':rowdata[9],
                    'location':rowdata[10],
                    'portion_size':rowdata[11],
                    'portion_measurement_unit':rowdata[12],
                    'photograph':rowdata[13],
                    'food_tags_breakout':rowdata[14],
                    'client_drink_input':rowdata[15],
                    'drink_size_numerator':rowdata[16],
                    'drink_size_denominator':rowdata[17],
                    'drink_input_breakout':rowdata[18],
                    'drink_tags_breakout':rowdata[19],
                    'flatulence_incidental':rowdata[20],
                    'flatulence_daily':rowdata[21],
                    'faeces':rowdata[22],
                    'discomfort_incidental':rowdata[23],
                    'discomfort_daily':rowdata[24],
                    'discomfort_descriptor':rowdata[25],
                    'reflux_incidental':rowdata[26],
                    'reflux_daily':rowdata[27],
                    'vomiting_incidental':rowdata[28],
                    'vomiting_daily':rowdata[29],
                    'sleep_quantity':rowdata[30],
                    'sleep_quality':rowdata[31],
                    'sleep_notes':rowdata[32],
                    'mental_state_mood':rowdata[33],
                    'exercise_duration':rowdata[34],
                    'exercise_type':rowdata[35],
                    'weight':rowdata[36],
                    'ad_hoc':rowdata[37]
                };
                //对同一行的修改只保留一次
                var j=0;
                for(;j<changes_list.length;j++){
                    if(changes_list[j].lid == log.lid){
                        changes_list[j] = log;
                        break;
                    }
                }
                if(j == changes_list.length){
                    changes_list.push(log);
                }



            }
        },
    data: data,
    // 37 columns
    colHeaders: [
        "Log id",
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
//        "Log id"
        {
            data: 0,
            type: "numeric",
            readOnly: true
        },
//        "Flag"
        {
            data: 1,
            type: "numeric"
        },
//        "Date"
        {
            data: 2,
            type: "date",
            correctFormat: true
        },
//        "Time"
        {
            data: 3,
            type: "time",
            correctFormat: true
        },
        {
            data: 4,
            type: "text"
        },
        {
            data: 5,
            type: "text"
        },
        {
            data: 6,
            type: "text"
        },
        {
            data: 7,
            type: "text"
        },
        {
            data: 8,
            type: "text"
        },
        {
            data: 9,
            type: "text"
        },
        {
            data: 10,
            type: "text"
        },
        {
            data: 11,
            type: "text"
        },
        {
            data: 12,
            type: "text"
        },
        {
            data: 13,
            type: "text"
        },
        {
            data: 14,
            type: "text"
        },
        {
            data: 15,
            type: "text"
        },
        {
            data: 16,
            type: "text"
        },
        {
            data: 17,
            type: "text"
        },
        {
            data: 18,
            type: "text"
        },
        {
            data: 19,
            type: "text"
        },
        {
            data: 20,
            type: "text"
        },
        {
            data: 21,
            type: "text"
        },
        {
            data: 22,
            type: "text"
        },
        {
            data: 23,
            type: "text"
        },
        {
            data: 24,
            type: "text"
        },
        {
            data: 25,
            type: "text"
        },
        {
            data: 26,
            type: "text"
        },
        {
            data: 27,
            type: "text"
        },
        {
            data: 28,
            type: "text"
        },
        {
            data: 29,
            type: "text"
        },
        {
            data: 30,
            type: "text"
        },
        {
            data: 31,
            type: "text"
        },
        {
            data: 32,
            type: "text"
        },
        {
            data: 33,
            type: "text"
        },
        {
            data: 34,
            type: "text"
        },
        {
            data: 35,
            type: "numeric"
        },
        {
            data: 36,
            type: "text"
        },
//        "Ad hoc"
        {
            data: 37,
            type: "text"
        }

    ],
    licenseKey: 'non-commercial-and-evaluation'// for non-commercial use only
});

