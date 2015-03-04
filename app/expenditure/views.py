from app import db
from app.expenditure.forms import ItemForm, GroupForm
from flask import Blueprint, render_template, g, redirect, url_for, flash, request
from app.expenditure.models import ExpenditureItem, ExpenditureGroup
from flask.ext.login import login_required, current_user

mod = Blueprint('expenditure', __name__, template_folder='templates', url_prefix='/expenditure')


@mod.route('/')
@login_required
def index():
    return render_template('expenditure.html', title='Expenditure')


@mod.route('/items/')
@login_required
def items():
    return render_template('items.html',
                           title='Expenditure Items',
                           items=ExpenditureItem.query.filter_by(user_id=g.user.id).order_by('title'))


@mod.route('/items/add/', methods=['GET', 'POST'])
@login_required
def item_add():
    form = ItemForm()
    if form.validate_on_submit():
        item = ExpenditureItem(title=form.title.data, user_id=g.user.id)
        db.session.add(item)
        db.session.commit()
        return redirect(url_for('expenditure.items'))
    return render_template('item_add.html', form=form, title='Add Expenditure Item')


@mod.route('/items/<int:item_id>/edit/', methods=['GET', 'POST'])
@login_required
def item_edit(item_id):
    item = ExpenditureItem.query.filter_by(id=item_id, user_id=g.user.id).first()
    if item is None:
        flash('Expenditure Item with ID %s not found' % item_id)
        return redirect(url_for('expenditure.items'))
    form = ItemForm(data={'title': item.title})
    if form.validate_on_submit():
        item.title = form.title.data.strip()
        db.session.add(item)
        db.session.commit()
        return redirect(url_for('expenditure.items'))
    return render_template('item_edit.html', form=form, title='Edit Expenditure Item')


@mod.route('/items/<int:item_id>/remove/', methods=['GET', 'POST'])
@login_required
def item_remove(item_id):
    item = ExpenditureItem.query.filter_by(id=item_id, user_id=g.user.id).first()
    if item is None:
        flash('Expenditure Item with ID %s not found' % item_id)
        return redirect(url_for('expenditure.items'))
    if request.method == 'POST':
        if '_remove_' in request.form:
            db.session.delete(item)
            db.session.commit()
        return redirect(url_for('expenditure.items'))
    return render_template('item_remove.html', title='Remove Expenditure Item', item=item)


@mod.route('/groups/')
@login_required
def groups():
    return render_template('groups.html',
                           title='Expenditure Groups',
                           groups=ExpenditureGroup.query.filter_by(user_id=g.user.id).order_by('title'))


@mod.route('/groups/add/', methods=['GET', 'POST'])
@login_required
def group_add():
    form = GroupForm()
    if form.validate_on_submit():
        item = ExpenditureGroup(title=form.title.data, user_id=g.user.id)
        db.session.add(item)
        db.session.commit()
        return redirect(url_for('expenditure.groups'))
    return render_template('group_add.html', form=form, title='Add Expenditure Group')


@mod.route('/groups/<int:group_id>/edit/', methods=['GET', 'POST'])
@login_required
def group_edit(group_id):
    group = ExpenditureGroup.query.filter_by(id=group_id, user_id=g.user.id).first()
    if group is None:
        flash('Expenditure Group with ID %s not found' % group_id)
        return redirect(url_for('expenditure.groups'))
    form = GroupForm(data={'title': group.title})
    if form.validate_on_submit():
        group.title = form.title.data.strip()
        db.session.add(group)
        db.session.commit()
        return redirect(url_for('expenditure.groups'))
    return render_template('group_edit.html', form=form, title='Edit Expenditure Group')


@mod.route('/groups/<int:group_id>/remove/', methods=['GET', 'POST'])
@login_required
def group_remove(group_id):
    group = ExpenditureGroup.query.filter_by(id=group_id, user_id=g.user.id).first()
    if group is None:
        flash('Expenditure Group with ID %s not found' % group_id)
        return redirect(url_for('expenditure.groups'))
    if request.method == 'POST':
        if '_remove_' in request.form:
            db.session.delete(group)
            db.session.commit()
        return redirect(url_for('expenditure.groups'))
    return render_template('group_remove.html', title='Remove Expenditure Group', group=group)


@mod.before_request
def before_request():
    g.user = current_user
