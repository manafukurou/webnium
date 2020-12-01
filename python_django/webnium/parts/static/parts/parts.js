
    
$(function(){

    Sortable.create(task_list, {
        animation: 150,
    });
    
    

    
    $('#btn-task').click(function() {

        var div = $('<div />',{class: 'd-flex p-2 bd-highlight m-2'} );
        var select_element = getTaskTypeSelectBox();
        div.append(select_element);
        $('#task_list').append(div);
    });
    //セレクトボックスが切り替わったら発動
    $(document).on('change', '.type_select', function(){
        $(this).data("");
        alert("aselect");
    });

    function getTaskTypeSelectBox(){

        var element = $('<select />',{class: 'type_select'});

         /// 各optionのテキストとvalue値の配列
        const optionCntList = [
            { text: '---select---', value: 'none' },
            { text: 'open url', value: 'open_url' },
            { text: 'click object', value: 'click_object' },
            { text: 'input param', value: 'input_param' },
      ]
        
        /// jQueryによるセレクトボックス初期化

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

});