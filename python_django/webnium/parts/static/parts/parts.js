$(function(){

    /// 各optionのテキストとvalue値の配列
    const optionCntList = [
        { text: '---select---', value: 'none' },
        { text: 'open url', value: 'input_url' },
        { text: 'click object', value: 'click_type' },
        { text: 'input param', value: 'input_value' },
    ];

    Sortable.create(task_list, {
        animation: 150,
    });
    
    $('#btn-task').click(function() {
        var div = $('<div />',{class: 'd-flex p-2 bd-highlight m-2'} );
        
        var select_element = getTaskTypeSelectBox();
        div.append(select_element);
        
        var input_value = getInputURL();
        div.append(input_value);

        var click_type = getClickTypeSelectBox();
        div.append(click_type);

        var input_value = getInputValue();
        div.append(input_value);

        $('#task_list').append(div);
    });

    //セレクトボックスが切り替わったら発動
    $(document).on('change', '.type_select', function(){
        var selected = $(this).val();
        var parent_div = $(this).parent();
        switchView(parent_div,selected)

    });

    function getTaskTypeSelectBox(){

        var element = $('<select />',{class: 'type_select'});

        var keys = Object.keys(optionCntList);
        keys.forEach(function(key, i){
            /// option要素を動的に生成＆追加
            var content = this[key];
            var option = $('<option>')
            .text(content['text'])
            .val(content['value']);
            element.append(option);
        }, optionCntList);
        return element;
    }
    function switchView(parent_div,selected){
        
        parent_div.find("div").hide();
        var selected_class_name = "."+selected;
        parent_div.find(selected_class_name).show();
    }
    function getInputURL(){

        var element = $('<div />',{class: 'input_url'}).append("a");
        element.hide();
        return element;
    }
    function getClickTypeSelectBox(){

        var element = $('<div />',{class: 'click_type'}).append("b");
        element.hide();
        return element;
    }
    function getInputValue(){

        var element = $('<div />',{class: 'input_value'}).append("c");
        element.hide();
        return element;
    }
});