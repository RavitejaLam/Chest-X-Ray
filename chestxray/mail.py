def sendmail(user,out):
    # Python code to illustrate Sending mail with attachments
    # from your Gmail account

    # libraries to be imported
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders

    fromaddr = "15131a05b7@gvpce.ac.in"
    toaddr = user.email

    # instance of MIMEMultipart
    msg = MIMEMultipart()

    # storing the senders email address
    msg['From'] = fromaddr

    # storing the receivers email address
    msg['To'] = toaddr

    # storing the subject
    msg['Subject'] = "Chest X-Ray Result."

    # string to store the body of the mail
    body = """<td class="m_5487230226081184158cell" width="580">
  <table class="m_5487230226081184158table" style="margin-top:15px" width="580" cellspacing="0" cellpadding="0" border="0">
    <tbody>
      <tr>
        <td class="m_5487230226081184158logocell" width="254" bgcolor="#fafafa" align="center">
          <br class="m_5487230226081184158hide">
          <img src="http://www.solivar.com/images/logo_solivarlabs.png"
            alt="solivarlabs Logo" class="CToWUd" width="20%">
          <br>
          <br class="m_5487230226081184158hide">
        </td>
      </tr>
      <tr>
        <td>
          <u></u>
          <u></u>
          <table width="580" cellspacing="0" cellpadding="0" border="0">
            <tbody>
              <tr>
                <td style="border-radius:5px" width="580" bgcolor="#ffffff">
                  <table style="border:1px solid #e4e4e4;border-radius:5px" width="580" cellspacing="0" cellpadding="20" border="0">
                    <tbody>
                      <tr>
                        <td class="m_5487230226081184158contentblock" style="border-radius:5px" bgcolor="#ffffff">
                          <table style="margin-top:15px" width="535" cellspacing="0" cellpadding="10" border="0" align="center">
                            <tbody>
                              <tr>
                                <td class="m_5487230226081184158yield">

                                  <p>Hello {0},</p>


                                    <p><strong>Chest X-Ray Results</strong></p>
                                    <p>View Type: {1}</p>
                                    <p>Uploaded On: {2}</p>
                                    <p>Result: {3}</p>
                                    <p>Thanks for using our service.</p>
                                    <br>
                                    <img alt="chest-x-ray image" src="."+{4} height="30%">
                                    {4}
                                    <br>
                                    <p>Stay Healthy! Stay Strong!
                                    <br> Solivar Medicals Team</p>

                                </td>
                              </tr>
                            </tbody>
                          </table>
                        </td>
                      </tr>
                    </tbody>
                  </table>
                </td>
              </tr>
            </tbody>
          </table>
          <table width="100%" cellspacing="0" cellpadding="0" border="0">
            <tbody>
              <tr>
                <td>
                  <p style="color:#888888;font-size:12px;font-family:Helvetica,Arial,sans-serif;text-align:center;margin-top:15px;margin-bottom:15px;padding-top:0;padding-bottom:0;line-height:18px"
                    class="m_5487230226081184158reminder">
                  </p>

                  <p style="color:#9f9f9f;font-size:10px;font-family:Helvetica,Arial,sans-serif;text-align:center;margin-top:15px;margin-bottom:15px;padding-top:0;padding-bottom:0;line-height:18px"
                    class="m_5487230226081184158reminder">
                    Copyright © 2018 Solivar Medicals, All rights reserved.
                  </p>

                </td>
              </tr>
            </tbody>
          </table>
          <u></u>
          <u></u>
        </td>
      </tr>
    </tbody>
  </table>
</td>""".format(user.first_name,out.side,out.submitted_on,out.description,out.image)

    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'html'))

    # open the file to be sent
    filename = "."+out.image.url
    attachment = open(filename, "rb")

    # # instance of MIMEBase and named as p
    # p = MIMEBase('application', 'octet-stream')
    #
    # # To change the payload into encoded form
    # p.set_payload((attachment).read())
    #
    # # encode into base64
    # encoders.encode_base64(p)
    #
    # p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    #
    # # attach the instance 'p' to instance 'msg'
    # msg.attach(p)

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login(fromaddr, "007ravi...")

    # Converts the Multipart msg into a string
    text = msg.as_string()

    # sending the mail
    s.sendmail(fromaddr, toaddr, text)

    # terminating the session
    s.quit()