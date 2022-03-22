import base64
import os
import uuid

from odoo import fields, http, _
from odoo.http import request
from odoo.addons.website.controllers.main import Website
from werkzeug import urls
from odoo.addons.web_editor.controllers.main import Web_Editor
from werkzeug.exceptions import Forbidden, NotFound

from datetime import date

class Website(Website):
    @http.route('/qrcode-form', type="http", auth='public', website=True)
    def qrcode_webform(self, **kw):
        print("Execution Here.........................")
        values, errors = {}, {}
        partner = request.env.user.partner_id
        # contacts = request.env['res.partner.category'].sudo().search([])
        values.update({
            'partner': partner,
        })
        return http.request.render('zts_webform_verification.upload_webform_details', values)

    @http.route(['/form-submit'], type='http', auth='public', website=True)
    def upload_webform(self, redirect=None, **kw):
        res_partner = request.env['res.partner']
        tag_id = request.env['res.partner.category'].sudo().search([('name', '=', 'BYH')], limit=1)
        print("86............", kw)
        partner_record = {
            'phone': kw.get('phone'),
            'comment': kw.get('description') or False,
            'email': kw.get('email_from'),
            'name': kw.get('contact_name'),
            'category_id': tag_id or False,
        }
        print(partner_record)
        res_partner_temp = request.env['res.partner.temp']
        rec = res_partner_temp.sudo().create(partner_record)
        # send email verification
        rec._send_profile_validation_email(**kw)

        return http.request.render('zts_webform_verification.form_user_thanks', {})


    @http.route('/profile/validate_email', type='http', auth='public', website=True, sitemap=False)
    def validate_email(self,token, user_id, email, **kwargs):
        res_partner_temp = request.env['res.partner.temp']
        res_partner_temp_rec = res_partner_temp.sudo().browse(int(user_id))
        res_partner_temp_data = {
            'phone': res_partner_temp_rec.phone,
            'comment': res_partner_temp_rec.comment or False,
            'email': res_partner_temp_rec.email,
            'name': res_partner_temp_rec.name,
            'category_id': res_partner_temp_rec.category_id or False,
        }
        res_partner= request.env['res.partner']

        karma_val = res_partner_temp.sudo().browse(int(user_id)).karma
        done = res_partner_temp.sudo().browse(int(user_id))._process_profile_validation_token(token, email)
        if done:
            request.session['validation_email_done'] = True
        if(karma_val == 0):
            url = kwargs.get('redirect_url', '/profile/validated')
            res = res_partner.sudo().create(res_partner_temp_data)
        else:
            url = kwargs.get('redirect_url', '/profile/already-validated')


        return request.redirect(url)

    @http.route('/profile/validated', type="http", auth='public', website=True)
    def validate_email_message1(self):
        return http.request.render('zts_webform_verification.form_confirm_validate')

    @http.route('/profile/already-validated', type="http", auth='public', website=True)
    def validate_email_message2(self):
        return http.request.render('zts_webform_verification.form_confirm_already_validate')

    # @http.route('/profile/send_validation_email', type='json', auth='public', website=True)
    # def send_validation_email(self, **kwargs):
    #     if request.env.uid != request.website.user_id.id:
    #         request.env.user._send_profile_validation_email(**kwargs)
    #     request.session['validation_email_sent'] = True
    #     return True
    #
    #
    # @http.route('/profile/validate_email/close', type='json', auth='public', website=True)
    # def validate_email_done(self, **kwargs):
    #     request.session['validation_email_done'] = False
    #     return True
