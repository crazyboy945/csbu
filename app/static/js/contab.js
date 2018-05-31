/*btnClick = {
    "click #btn_test": function(e, value, row, index) {
        layer.open({
            type: 2,
            title: '合同信息修改',
            maxmin: false,
            area: ['800px', '460ox'],
            content: '/contract/edit/' + int(row.id),

        });
    }

};
*/
var TableObj = {
    //初始化Table
    oTableInit: function() {

        $table = $('#table');　　
        $table.bootstrapTable({
            //data: jsonData,
            dataType: "json",
            striped: true,
            method: 'get',
            toolbar: "#toolbar",
            contentType: "application/x-www-form-urlencoded",
            cache: false,
            url: '/contract/list',
            pagination: true,
            sidePagination: "server",
            pagenumber: 1,
            pageSize: 10,
            queryParams: function(params) {

                return {
                    limit: params.limit, // 每页要显示的数据条数
                    offset: params.offset, // 每页显示数据的开始行号
                    sort: params.sort, // 要排序的字段
                    sortOrder: params.order, // 排序规则
                    dept: $("#dept").val(),
                    year: $("#year").val(),
                    month: $("#month").val()
                }
            },

            showToggle: false,
            cardview: true,
            pageList: [10, 25, 50, 100],
            fixedColumns: true,
            fixedNumber: 3,
            showFooter: true,
            showExport: true,
            columns: [
                [{
                        title: '操作',
                        field: 'id',
                        align: 'center',
                        valign: "middle",
                        halign: "center",
                        width: "150px",
                        //envents: btnClick,
                        formatter: function(value, row, index) {
                            var d = '<button id="del" title="删除当前合同！" class="btn btn-primary" onclick="del(' + row.id +
                                ')"><span class="glyphicon glyphicon-trash" aria-hidden="true"></span></button>';
                            var p = '<button id="editp" class="btn btn-primary" onclick="editprice(' + row.id +
                                ')" title="维护开票/回款信息"><span class="glyphicon glyphicon-yen" aria-hidden="true"></span></button>&nbsp;';

                            var b = '<button id="editc" title="修改合同基本信息" class="btn btn-primary" onclick="editcon(' + row.id +
                                ')"><span class="glyphicon glyphicon-pencil"></button>&nbsp;';
                            return b + p + d;
                        }
                    },

                    {
                        field: 'contract_number',
                        title: '合同号',
                        valign: "middle",
                        halign: "center",
                        align: "left",
                        sortable: true,
                        width: "120px"

                    }, {
                        field: 'department',
                        title: '领域',
                        valign: "middle",
                        halign: "center",
                        align: "left",
                        sortable: true,
                        width: "120px"

                    }, {
                        field: 'custom',
                        title: "客户",
                        valign: "middle",
                        halign: "center",
                        sortable: true,
                        align: "left",
                        width: "200px"

                    }, {
                        field: 'project_name',
                        title: "项目名称",
                        valign: "middle",
                        halign: "center",
                        align: "left",
                        sortable: true,
                        width: "300px",

                    }, {
                        field: 'contract_date',
                        title: "合同日期",
                        valign: "middle",
                        halign: "center",
                        align: "center",
                        sortable: true,
                        width: "120px"
                    }, {
                        field: 'contract_price',
                        title: "合同金额",
                        halign: "center",
                        valign: "middle",
                        align: "right",
                        width: "120px",
                        footerFormatter: function(value) {
                            var count = 0;
                            for (var
                                    i in value) {
                                count += Number(value[i].contract_price);
                            }
                            return Math.round(count * 100) / 100;
                        }
                    }, {
                        field: 'bill_date',
                        title: "开票日期",
                        halign: "center",
                        valign: "middle",
                        align: "center",
                        width: "120px"
                    }, {
                        field: 'bill_price',
                        title: "开票金额",
                        halign: "center",
                        valign: "middle",
                        align: "right",
                        width: "120",
                        footerFormatter: function(value) {
                            var count = 0;
                            for (var
                                    i in value) {
                                count += Number(value[i].bill_price);
                            }
                            return Math.round(count * 100) / 100;
                        }
                    }, {
                        field: 'repayment_date',
                        title: "回款日期",
                        halign: "center",
                        valign: "middle",
                        align: "center",
                        width: "120"
                    }, {
                        field: 'repayment',
                        title: "回款金额",
                        halign: "center",
                        valign: "middle",
                        align: "right",
                        width: "120",
                        footerFormatter: function(value) {
                            var count = 0;
                            for (var
                                    i in value) {
                                count += Number(value[i].repayment);
                            }
                            return Math.round(count * 100) / 100;
                        }
                    },

                    {
                        field: 'total_bill',
                        title: "累计开票",
                        halign: "center",
                        valign: "middle",
                        align: "right",
                        width: "120",
                        footerFormatter: function(value) {
                            var count = 0;
                            for (var
                                    i in value) {
                                count += Number(value[i].total_bill);
                            }
                            return Math.round(count * 100) / 100;
                        }
                    }, {
                        field: 'total_payment',
                        title: "累计回款",
                        halign: "center",
                        valign: "middle",
                        align: "right",
                        width: "120",
                        footerFormatter: function(value) {
                            var count = 0;
                            for (var
                                    i in value) {
                                count += Number(value[i].total_payment);
                            }
                            return Math.round(count * 100) / 100;
                        }
                    }, {
                        field: 'nbill_date',
                        title: "下次开票日期",
                        halign: "center",
                        valign: "middle",
                        align: "center",
                        width: "120"
                    }, {
                        field: 'nbill_price',
                        title: "下次开票金额",
                        halign: "center",
                        valign: "middle",
                        align: "right",
                        width: "120",
                        footerFormatter: function(value) {
                            var count = 0;
                            for (var
                                    i in value) {
                                count += Number(value[i].nbill_price);
                            }
                            return Math.round(count * 100) / 100;
                        }
                    }, {
                        field: 'npayment_date',
                        title: "下次回款日期",
                        halign: "center",
                        valign: "middle",
                        align: "right",
                        width: "120"
                    }, {
                        field: 'nrepayment',
                        title: "下次回款金额",
                        halign: "center",
                        valign: "middle",
                        align: "right",
                        width: "120",
                        footerFormatter: function(value) {
                            var count = 0;
                            for (var
                                    i in value) {
                                count += Number(value[i].npayment_date);
                            }
                            return Math.round(count * 100) / 100;
                        }
                    },
                ]
            ]
        });


    },
    EditCon: function(row) {

        layer.open({
            type: 2,
            title: '合同信息修改',
            maxmin: false,
            area: ['800px', '460ox'],
            content: '/contract/edit/' + int(row.id),

        });

    }

};